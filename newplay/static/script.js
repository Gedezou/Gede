
// // Get the nav by id
// var pNav = document.getElementById("Nav");

// function toggleSubNav(eID) {
//   try {
//     // Get all the top-level items and get the buttons
//     var allButtons = document.querySelectorAll("#Nav > ul > li > a + button");
//     // Get all sub-menus
//     var allSubMenus = document.querySelectorAll("#Nav > ul > li > a + button + ul");
//     if (eID !== "") {
//       // Get the button
//       var toggle = document.querySelector("#" + eID);
//       // Find out what the button controls
//       var subMenuIdent = toggle.getAttribute("aria-controls");
//       // Get that thing it controls
//       var subMenu = document.getElementById(subMenuIdent);
//       // Toggle text and expanded state
//       if (toggle.getAttribute("aria-expanded") === "false") {
//         // Loop through all buttons and mark as closed
//         for (var i = 0; i < allButtons.length; i++) {
//           allButtons[i].setAttribute("aria-expanded", "false");
//           // allButtons[i].setAttribute("aria-label", "Show");
//         //   allButtons[i].innerHTML = arrowShow;
//         }
//         // Now mark the chosen button as opened
//         toggle.setAttribute("aria-expanded", "true");
//         // toggle.setAttribute("aria-label", "Hide");
//       } else {
//         // Close chosen button; no need to loop through rest of nodes
//         toggle.setAttribute("aria-expanded", "false");
//         // toggle.setAttribute("aria-label", "Show");
//       }
//       // Expand or collapse
//       if (subMenu.style.display === "none") {
//         // Hide all submenus
//         for (var i = 0; i < allSubMenus.length; i++) {
//           allSubMenus[i].style.display = "none";
//         }
//         // Show chosen submenu
//         subMenu.style.display = "block";
//       } else {
//         // Close chosen menu; no need to loop through rest of nodes
//         subMenu.style.display = "none";
//       }
//     }
//     if (eID !== "") {
//     } else {
//       // Hide all submenus
//       for (var i = 0; i < allSubMenus.length; i++) {
//         allSubMenus[i].style.display = "none";
//       }
//       // Loop through all buttons and mark as closed
//       for (var i = 0; i < allButtons.length; i++) {
//         allButtons[i].setAttribute("aria-expanded", "false");
//         // allButtons[i].setAttribute("aria-label", "Show");
//         // allButtons[i].innerHTML = arrowShow;
//       }
//     }
//   } catch (e) {
//     console.log("toggleSubNav(): " + e);
//   }
//   const toggleButton = document.getElementById("toggleSubNav"); 
// const subNav = document.getElementById("subNav"); 
// // Add a click event listener to the toggle button 
// toggleButton.addEventListener("click", () => { 
//   // Toggle the "hidden" class on the sub-navigation 
//   subNav.classList.toggle("hidden"); }); 
//   // Close the sub-navigation when clicking outside of it 
//   document.addEventListener("click", 
//   (e) => { if (subNav.classList.contains("hidden")) 
//   return; if (!subNav.contains(e.target) && e.target !== toggleButton)
//  { subNav.classList.add("hidden"); } });
// }

// document.onkeydown = function(evt) {
//   evt = evt || window.event;
//   var isEscape = false;
//   if ("key" in evt) {
//     isEscape = evt.key == "Escape" || evt.key == "Esc";
//   } else {
//     isEscape = evt.keyCode == 27;
//   }
//   if (isEscape) {
//     //alert("Escape");
//     toggleSubNav("hidden");
//   }
//   function handleBlur(event) {
//     var menuContainsFocus = rootNode.contains(event.relatedTarget);
//     if (!menuContainsFocus && isOpen) {
//       closeDropdownNav();
//     }
//   };
// };






// function kalEl(settings = {}) {
//     const pad = (val) => (val + 1).toString().padStart(2, '0');
//     const render = (date, locale) => {
//       const month = date.getMonth();
//       const year = date.getFullYear();
//       const numOfDays = new Date(year, month + 1, 0).getDate();
//       const renderToday = (year === config.today.year) && (month === config.today.month);
  
//       return `<kal-el data-firstday="${config.info.firstDay}">
//         <time datetime="${year}-${(pad(month))}">${new Intl.DateTimeFormat(locale, { month: 'long'}).format(date)} <i>${year}</i></time>
//         <ul>${weekdays(config.info.firstDay,locale).map(name => `<li><abbr title="${name.long}">${name.short}</abbr></li>`).join('')}</ul>
//         <ol>
//         ${[...Array(numOfDays).keys()].map(i => {
//           const cur = new Date(year, month, i + 1);
//           let day = cur.getDay(); if (day === 0) day = 7;
//           const today = renderToday && (config.today.day === i + 1) ? ' data-today':'';
//           return `<li data-day="${day}"${today}${i === 0 || day === config.info.firstDay ? ` data-weeknumber="${new Intl.NumberFormat(locale).format(getWeek(cur))}"`:''}${config.info.weekend.includes(day) ? ` data-weekend`:''}>
//             <time datetime="${year}-${(pad(month))}-${pad(i)}" tabindex="0">${new Intl.NumberFormat(locale).format(i + 1)}</time>
//           </li>`
//         }).join('')}
//         </ol>
//       </kal-el>`;
//     }
  
//     const weekdays = (firstDay, locale) => {
//       const date = new Date(0);
//       const arr = [...Array(7).keys()].map(i => {
//         date.setDate(5 + i)
//         return {
//             long: new Intl.DateTimeFormat([locale], { weekday: 'long'}).format(date),
//             short: new Intl.DateTimeFormat([locale], { weekday: 'short'}).format(date)
//           }
//       })
//       for (let i = 0; i < 8 - firstDay; i++) arr.splice(0, 0, arr.pop());
//       return arr;
//     }
  
//     const today = new Date();
//     const config = Object.assign({ locale: (document.documentElement.getAttribute('lang') || 'en-US'), today: { day: today.getDate(), month: today.getMonth(), year: today.getFullYear() } }, settings);
//     const date = config.date ? new Date(config.date) : today;
//     if (!config.info) config.info = new Intl.Locale(config.locale).weekInfo || { firstDay: 7, weekend: [6, 7] };
//     return config.year ? [...Array(12).keys()].map(i => render(new Date(date.getFullYear(), i, date.getDate()), config.locale, date.getMonth())).join('') : render(date, config.locale)
//   }
  
//   function getWeek(cur) {
//     const date = new Date(cur.getTime());
//     date.setHours(0, 0, 0, 0);
//     date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
//     const week = new Date(date.getFullYear(), 0, 4);
//     return 1 + Math.round(((date.getTime() - week.getTime()) / 86400000 - 3 + (week.getDay() + 6) % 7) / 7);
//   }
  
//   /* Init Demo */
//   app.innerHTML = kalEl(app.dataset);
//   lang.addEventListener('change', () => {
//     document.documentElement.lang = lang.value;
//     app.innerHTML = kalEl(app.dataset)
//   });

// const borderImageWidthInput = document.querySelector(
//   "#border-image-width-input"
// );
// const borderWidthInput = document.querySelector("#border-width-input");
// const borderOutsetInput = document.querySelector("#border-outset-input");
// const rootElement = document.querySelector(":root");
// const rootStyle = getComputedStyle(rootElement);

// rootElement.style.cssText = rootElement.style.cssText = `--border-image-width: ${borderImageWidthInput.value};
//     --border-image-outset: ${borderOutsetInput.value};
//     --border-width: ${borderWidthInput.value};
//     `;

// borderImageWidthInput.addEventListener("change", () => {
//   rootElement.style.cssText = `--border-image-width: ${
//     borderImageWidthInput.value
//   };
//     --border-image-outset: ${rootStyle.getPropertyValue(
//       "--border-image-outset"
//     )};
//     --border-width: ${rootStyle.getPropertyValue("--border-width")};
//     `;
// });

// borderWidthInput.addEventListener("change", () => {
//   rootElement.style.cssText = `--border-image-width: ${rootStyle.getPropertyValue(
//     "--border-image-width"
//   )};
//     --border-image-outset: ${rootStyle.getPropertyValue(
//       "--border-image-outset"
//     )};
//     --border-width: ${borderWidthInput.value};
//     `;
// });

// borderOutsetInput.addEventListener("change", () => {
//   rootElement.style.cssText = `--border-image-width: ${rootStyle.getPropertyValue(
//     "--border-image-width"
//   )};
//     --border-image-outset: ${borderOutsetInput.value};
//     --border-width: ${rootStyle.getPropertyValue("--border-width")};
//     `;
// });