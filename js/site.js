(function () {
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll("[data-faq]").forEach(function (item) {
    var button = item.querySelector("button");
    var panel = item.querySelector("[data-faq-panel]");
    if (!button || !panel) return;
    button.addEventListener("click", function () {
      var open = button.getAttribute("aria-expanded") === "true";
      button.setAttribute("aria-expanded", open ? "false" : "true");
      panel.hidden = open;
    });
  });

  document.querySelectorAll("[data-cookie-choice]").forEach(function (button) {
    button.addEventListener("click", function () {
      try {
        localStorage.setItem("ukcd_cookie", button.getAttribute("data-cookie-choice"));
      } catch (e) {}
      document.documentElement.classList.add("cookies-set");
    });
  });

  var form = document.querySelector("[data-contact]");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }
      form.querySelector("[data-fields]").hidden = true;
      form.querySelector("[data-sent]").hidden = false;
    });
  }
})();
