// @ts-check
document.addEventListener("DOMContentLoaded", function () {
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
    return;
  }

  form.addEventListener("submit", (event) => {
    console.log("submit form");
    event.preventDefault();
    if (form instanceof HTMLFormElement) {
      const formData = new FormData(form);
      // for (const pair of formData) {
      //   formData.append(pair[0], pair[1]);
      // }
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
