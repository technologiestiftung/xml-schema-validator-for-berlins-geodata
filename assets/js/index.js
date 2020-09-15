// @ts-check
document.addEventListener("DOMContentLoaded", function () {
  let fileContent = undefined;
  const target = document.querySelector("#results");
  if (!target) {
    throw new Error("Could not find target div (#results) for results");
  }

  const resframe = document.querySelector("iframe#result-iframe");
  if (resframe) {
    if (resframe instanceof HTMLElement) {
      resframe.style.display = "none";
    }
  }

  const form = document.querySelector("#form");
  if (!form) {
    throw new Error("Could not find form element (#form)");
  }

  const textArea = document.querySelector("textarea#txt");
  if (!textArea) {
    throw new Error("Could not find textarea#txt");
  }
  const fileUpload = document.querySelector("input#xml");
  if (!fileUpload) {
    throw new Error("Could not find file input element");
  }

  fileUpload.addEventListener(
    "change",
    function () {
      const fileList = this.files;
      const firstFile = fileList[0];
      // TODO: Can we validate that the file is an gml file?
      // below is just the solution for an xml file
      // if (firstFile.type !== "application/xml") {
      //   throw new Error("This is not an xml");
      // }
      const reader = new FileReader();
      reader.readAsText(firstFile, "UTF-8");
      reader.onerror = () => {
        throw new Error("could not read file");
      };
      reader.onload = (e) => {
        const xml = e.target.result;
        fileContent = xml;
        // @ts-ignore
        textArea.value = fileContent;
        // @ts-ignore
        // we could empty the file list here, but it would
        // create confusion for the user i guess
        // fileUpload.value = "";
      };
    },
    false
  );
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (form instanceof HTMLFormElement) {
      const formData = new FormData(form);
      // uf we have something in txt entry we don't need to
      // send the file over
      if (formData.get("txt") !== undefined) {
        formData.delete("xml"); // that's why we remove it
        // below while loop is just for verification that the
        // selected file is actually gone
        const it = formData.keys();
        let result = it.next();
        // formData.set("txt", fileContent);
        while (!result.done) {
         // console.log(result.value);
          result = it.next();
        }
      }
      fetch(form.action, {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            // throw error
            // give warning
            // do something
            return;
          }
          //form.reset();
          return response.json();
        })
        .then((json) => {
          //console.log(json);
          if (target instanceof HTMLElement) {
            target.innerHTML = "";   
            const br = document.createElement("br");   
            for (var key in json) {
              if (json.hasOwnProperty(key)) {
                if (key === "status") {
                  const h4 = document.createElement("h4");
                  h4.classList.add("bold");
                  h4.textContent = json.message;
                  h4.style.paddingBottom = "1rem";
                  if (json[key] === "valid") {                   
                    h4.style.color = "#213A8F";
                    target.appendChild(h4);          
                    target.appendChild(br);
                  } else {
                    h4.style.color = "#E60032";
                    target.appendChild(h4);          
                    target.appendChild(br);
                  }
                }
              }
            }
            for (var key in json) {
              if (json.hasOwnProperty(key)) {
                if (key !== "message" && key !== "status") {
                  const p = document.createElement("p");
                  p.style.paddingBottom = "0.5rem";
                  const span = document.createElement("span");
                  span.style.color = "#E60032";
                  span.textContent = "Fehler in Zeile " + key + ": ";
                  const span2 = document.createElement("span");
                  span2.classList.add("headline-04");
                  span2.textContent = json[key];
                  p.appendChild(span);
                  p.appendChild(span2);
                  target.appendChild(p);
                }
              }
            }
          }
        })
        .catch(console.error);
    }
  });
});
