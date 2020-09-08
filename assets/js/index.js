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
        formData.set("txt", fileContent);
        while (!result.done) {
          console.log(result.value);
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
          form.reset();
          return response.json();
        })
        .then((json) => {
          console.log(json);
          if (target instanceof HTMLElement) {
            target.innerText = json.message;
          }
        })
        .catch(console.error);

      // do something with json response
    }
  });
});
