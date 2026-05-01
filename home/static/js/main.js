const burger = document.querySelector(".burger");
const nav = document.querySelector(".header__nav");
const overlay = document.querySelector(".nav-overlay");

function toggleMenu(open) {
  burger.classList.toggle("is-active", open);
  nav.classList.toggle("is-open", open);
  overlay.classList.toggle("is-visible", open);
  burger.setAttribute("aria-expanded", open);
  document.body.style.overflow = open ? "hidden" : "";
}

// БУРГЕР
burger.addEventListener("click", () => {
  const isOpen = nav.classList.contains("is-open");
  toggleMenu(!isOpen);
});

overlay.addEventListener("click", () => toggleMenu(false));

const esc = document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") toggleMenu(false);
});

const heder__link = document
  .querySelectorAll(".heder__nav__link")
  .forEach((link) => {
    link.addEventListener("click", () => toggleMenu(false));
  });

const gallery = document.querySelectorAll("[data-lightbox]").forEach((item) => {
  item.addEventListener("click", () => {
    toggleMenu(false);
  });
});

// LIGHTBOX
lightbox.option({
  resizeDuration: 200,
  wrapAround: true,
  disableScrolling: true,
});

// MAP
const lat = 51.3324911;
const lng = 26.630372;

const map = L.map("location__map").setView([lat, lng], 17);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution: "© OpenStreetMap",
}).addTo(map);

L.marker([lat, lng])
  .addTo(map)
  .bindPopup("<b>вул. Льва Толстого 22б</b><br>м. Сарни, Рівненська обл.")
  .openPopup();

// INPUT MASK
Inputmask("+380 (99) 999-99-99").mask(document.getElementById("f-phone"));

// POPOVER
const popover = document.getElementById("mypopover");

popover.addEventListener("toggle", (e) => {
  document.body.style.overflow = e.newState === "open" ? "hidden" : "";
});

// VALIDATION
const validation = new JustValidate("#training-form", {
  errorFieldCssClass: "is-invalid",
  errorLabelCssClass: "popover__error",
  successFieldCssClass: "is-valid",
  validateBeforeSubmitting: true,
});

validation
  .addField("#f-name", [
    { rule: "required", errorMessage: "Введіть ім'я" },
    { rule: "minLength", value: 2, errorMessage: "Мінімум 2 символи" },
  ])
  .addField("#f-surname", [
    { rule: "required", errorMessage: "Введіть прізвище" },
    { rule: "minLength", value: 2, errorMessage: "Мінімум 2 символи" },
  ])
  .addField("#f-patronymic", [
    { rule: "required", errorMessage: "Введіть по батькові" },
    { rule: "minLength", value: 2, errorMessage: "Мінімум 2 символи" },
  ])
  .addField("#f-phone", [
    { rule: "required", errorMessage: "Введіть номер телефону" },
    {
      rule: "function",
      validator: () => {
        return document.getElementById("f-phone").inputmask.isComplete();
      },
      errorMessage: "Введіть повний номер",
    },
  ])
  .addField("#f-time", [
    { rule: "required", errorMessage: "Вкажіть час тренування" },
  ])
  .addField("#f-type", [
    { rule: "required", errorMessage: "Оберіть тип тренування" },
  ])
  .onSuccess(async () => {
    const form = document.getElementById("training-form");
    const btn = form.querySelector(".popover__submit");
    const message = document.getElementById("popover-message");

    btn.disabled = true;
    btn.textContent = "Відправляємо…";
    message.className = "popover__message";
    message.textContent = "";

    const data = Object.fromEntries(new FormData(form));

    try {
      const res = await fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
        body: JSON.stringify(data),
      });

      const result = await res.json();

      if (result.success) {
        message.textContent =
          "✓ Дякуємо! Ваш запис прийнято. Ми зв'яжемось з вами.";
        message.className = "popover__message popover__message--success";
        form.reset();

        form.querySelectorAll(".is-valid, .is-invalid").forEach((el) => {
          el.classList.remove("is-valid", "is-invalid");
        });

        setTimeout(() => {
          document.getElementById("mypopover").hidePopover();
          message.className = "popover__message";
          message.textContent = "";
        }, 2500);
      } else {
        throw new Error("failed");
      }
    } catch {
      message.textContent =
        "✗ Помилка! Спробуйте ще раз або зателефонуйте нам.";
      message.className = "popover__message popover__message--error";
    } finally {
      btn.disabled = false;
      btn.textContent = "Записатись";
    }
  });
