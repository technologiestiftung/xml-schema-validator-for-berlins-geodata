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
    throw new Error("Could not find form element (#form)");
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (form instanceof HTMLFormElement) {
      const formData = new FormData(form);

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
