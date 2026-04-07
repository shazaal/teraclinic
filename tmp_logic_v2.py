import os

def main():
    file_path = "c:\\webbbbb\\works\\tera_clinic\\index.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Step indicators
    indicators_old = """<div class="flex flex-row md:flex-col gap-2 md:gap-0 space-x-2 md:space-x-0 md:space-y-6 overflow-x-auto no-scrollbar pb-2 md:pb-0 w-full" id="stepIndicators">
          <div class="flex items-center gap-2 md:gap-4 step-ind active shrink-0" id="ind-1">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs bg-white text-[#2563EB]">1</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Info</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-2">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">2</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Service</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-3">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">3</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Mode</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-4">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">4</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Schedule</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-5">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">5</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Pay</p>
          </div>
        </div>"""

    indicators_new = """<div class="flex flex-row md:flex-col gap-2 md:gap-0 space-x-2 md:space-x-0 md:space-y-6 overflow-x-auto no-scrollbar pb-2 md:pb-0 w-full" id="stepIndicators">
          <div class="flex items-center gap-2 md:gap-4 step-ind active shrink-0" id="ind-1">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs bg-white text-[#2563EB]">1</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Phone</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-2">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">2</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Profile</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-3">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">3</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Service</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-4">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">4</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Mode</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-5">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">5</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Time</p>
          </div>
          <div class="flex items-center gap-2 md:gap-4 step-ind opacity-50 shrink-0" id="ind-6">
            <span class="w-6 h-6 md:w-8 md:h-8 rounded-full border-2 border-white flex items-center justify-center font-bold text-[10px] md:text-xs text-white">6</span>
            <p class="text-[10px] md:text-[11px] font-bold uppercase tracking-wider text-white">Pay</p>
          </div>
        </div>"""

    content = content.replace(indicators_old, indicators_new)

    # 2. Extract step panes and replace safely
    
    # 2a. Modify step-5 -> step-6
    content = content.replace('<div class="step-pane p-6 md:p-12 hidden" id="step-5">', '<div class="step-pane p-6 md:p-12 hidden" id="step-6">')
    
    # 2b. Modify step-4 -> step-5
    content = content.replace('<div class="step-pane p-6 md:p-12 hidden" id="step-4">', '<div class="step-pane p-6 md:p-12 hidden" id="step-5">')
    
    # 2c. Modify step-3 -> step-4
    content = content.replace('<div class="step-pane p-6 md:p-12 hidden" id="step-3">', '<div class="step-pane p-6 md:p-12 hidden" id="step-4">')
    
    # 2d. Modify step-2 -> step-3
    content = content.replace('<div class="step-pane p-6 md:p-12 hidden" id="step-2">', '<div class="step-pane p-6 md:p-12 hidden" id="step-3">')
    
    # 2e. Modify step-1 -> step-2
    content = content.replace('<div class="step-pane p-6 md:p-12 block" id="step-1">', '<div class="step-pane p-6 md:p-12 hidden" id="step-2">')

    # 2f. Phone input removal from Profile
    content = content.replace('              <input type="tel" name="phone" placeholder="WhatsApp Number" required class="w-full p-4 border-2 border-slate-100 rounded-2xl outline-none focus:border-blue-500" />\n', "")
    content = content.replace('<input type="text" name="name" placeholder="Full Name"', '<input type="text" id="userName" name="name" placeholder="Full Name"')
    content = content.replace('<input type="number" name="age" placeholder="Age"', '<input type="number" id="userAge" name="age" placeholder="Age"')
    content = content.replace('<input type="text" name="place" placeholder="Place / City"', '<input type="text" id="userPlace" name="place" placeholder="Place / City"')
    
    # 3. Add `isReturning` input field and the new `step-1` Phone pane
    new_step_1 = """          <div class="step-pane p-6 md:p-12 block" id="step-1">
            <div class="mb-8">
              <h3 class="text-2xl font-bold text-slate-800">Welcome Back</h3>
              <p class="text-slate-500 mt-2">Enter your phone number to quickly book your session.</p>
            </div>
            <div class="space-y-4">
              <label class="block text-xs font-bold text-blue-600 uppercase tracking-widest">WhatsApp Number</label>
              <input type="tel" id="mainPhone" name="phone" placeholder="+91 00000 00000" required 
                class="w-full p-5 border-2 border-slate-100 rounded-[20px] outline-none focus:border-blue-500 text-xl font-medium" />
              <p id="searchingText" class="hidden text-sm text-blue-600 font-medium animate-pulse">Checking your records...</p>
            </div>
          </div>"""
            
    content = content.replace('<input type="hidden" name="selected_date" id="inputDate" />', '<input type="hidden" name="selected_date" id="inputDate" />\n        <input type="hidden" name="is_returning_customer" id="isReturning" value="false" />')
    
    target_scrollbar = '<div class="flex-1 relative overflow-y-auto custom-scrollbar">'
    content = content.replace(target_scrollbar, target_scrollbar + "\n" + new_step_1)

    # 4. Modify 'modalNext' button 
    content = content.replace('onclick="changeStep(1)">Continue</button>', 'onclick="handleInitialNext()">Continue</button>')

    # 5. JAVASCRIPT: Safely replace the block 
    # Use split and join to find the exact `<script>` tag associated with the modal logic
    # Look for "let activeStep = 1;"
    
    script_start = content.find('<script>\n  let activeStep = 1;')
    if script_start == -1:
        script_start = content.find('<script>\n      let activeStep = 1;')
        if script_start == -1:
            # Fallback exact search
            script_start = content.find('let activeStep = 1;')
            script_start = content.rfind('<script>', 0, script_start)
    
    # ensure we only match to </script> belonging to this block
    if script_start != -1:
        script_end = content.find('</script>', script_start) + 9
        
        script_new = """<script>
  let activeStep = 1;
  let isChecking = false;

  // SIMULATED DATABASE
  const dummyDB = {
    "8590925353": { name: "Shasal", age: 24, place: "Kannur", gender: "Male" }
  };

  async function handleInitialNext() {
    if (activeStep === 1) {
      const phoneInput = document.getElementById("mainPhone").value.trim();
      if (!phoneInput) return alert("Please enter your number");

      document.getElementById("searchingText").classList.remove("hidden");
      isChecking = true;

      setTimeout(() => {
        document.getElementById("searchingText").classList.add("hidden");
        isChecking = false;

        if (dummyDB[phoneInput]) {
          const user = dummyDB[phoneInput];
          document.getElementById("userName").value = user.name;
          document.getElementById("userAge").value = user.age;
          document.getElementById("userPlace").value = user.place;
          document.getElementById("isReturning").value = "true";
          
          changeStep(2); // Jump from step 1 to step 3 skips 1 step => delta of +2
        } else {
          document.getElementById("isReturning").value = "false";
          changeStep(1); // Normal next
        }
      }, 800);
    } else {
      changeStep(1);
    }
  }

  let currentMonth = new Date().getMonth();
  let currentYear = new Date().getFullYear();
  let selectedDateStr = "";

  function openBookingModal() {
    document.getElementById("bookingModal").classList.remove("hidden");
    document.body.style.overflow = "hidden";
    renderCalendar();
  }

  function closeBookingModal() {
    document.getElementById("bookingModal").classList.add("hidden");
    document.body.style.overflow = "auto";
  }

  function autoNext() {
    setTimeout(() => changeStep(1), 400);
  }

  function renderCalendar() {
    const grid = document.getElementById("calendarGrid");
    const display = document.getElementById("monthDisplay");
    if (!grid) return;
    grid.innerHTML = "";
    const firstDay = new Date(currentYear, currentMonth, 1).getDay();
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    if (display) display.innerText = `${months[currentMonth]} ${currentYear}`;
    let startingPoint = firstDay === 0 ? 6 : firstDay - 1;
    for (let i = 0; i < startingPoint; i++) grid.innerHTML += `<div class="calendar-day empty"></div>`;
    for (let d = 1; d <= daysInMonth; d++) {
      const dateStr = `${currentYear}-${currentMonth + 1}-${d}`;
      const isToday = new Date().toDateString() === new Date(currentYear, currentMonth, d).toDateString();
      const isSelected = selectedDateStr === dateStr;
      grid.innerHTML += `<div class="calendar-day ${isToday ? 'today' : ''} ${isSelected ? 'selected' : ''}" onclick="selectDate('${dateStr}')">${d}</div>`;
    }
  }

  function selectDate(date) {
    selectedDateStr = date;
    const inputDate = document.getElementById("inputDate");
    if (inputDate) inputDate.value = date;
    renderCalendar();
  }

  function changeMonth(dir) {
    currentMonth += dir;
    if (currentMonth < 0) { currentMonth = 11; currentYear--; }
    if (currentMonth > 11) { currentMonth = 0; currentYear++; }
    renderCalendar();
  }

  function changeStep(delta) {
    if (delta > 0 && !validateStep(activeStep)) return;

    let nextStep = activeStep + delta;
    const isReturning = document.getElementById("isReturning").value === "true";

    // Handling skips for returning user
    if (delta > 0 && activeStep === 1 && isReturning && delta !== 2) {
      nextStep = 3; 
    } else if (delta < 0 && activeStep === 3 && isReturning) {
      nextStep = 1; 
    }

    if (document.getElementById(`step-${activeStep}`)) {
        document.getElementById(`step-${activeStep}`).classList.add("hidden");
    }
    if (document.getElementById(`ind-${activeStep}`)) {
        document.getElementById(`ind-${activeStep}`).classList.add("opacity-50");
        document.getElementById(`ind-${activeStep}`).querySelector("span").classList.remove("bg-white", "text-[#2563EB]");
    }

    activeStep = nextStep;

    if (document.getElementById(`step-${activeStep}`)) {
        document.getElementById(`step-${activeStep}`).classList.remove("hidden");
    }
    if (document.getElementById(`ind-${activeStep}`)) {
        document.getElementById(`ind-${activeStep}`).classList.remove("opacity-50");
        document.getElementById(`ind-${activeStep}`).querySelector("span").classList.add("bg-white", "text-[#2563EB]");
    }

    document.getElementById("modalBack").classList.toggle("invisible", activeStep === 1);
    document.getElementById("modalNext").classList.toggle("hidden", activeStep === 6);
    document.getElementById("modalSubmit").classList.toggle("hidden", activeStep !== 6);

    if (activeStep === 6) {
      const selected = document.querySelector('input[name="service"]:checked');
      const finalPriceEl = document.getElementById("finalPrice");
      if (finalPriceEl) {
        finalPriceEl.innerText = selected ? `₹${selected.dataset.price}` : "₹0";
      }
    }
  }

  function validateStep(step) {
    if (step === 1) return document.getElementById("mainPhone").value.trim() !== "";
    if (step === 2) {
      const inputs = document.getElementById("step-2").querySelectorAll("input[required]");
      return Array.from(inputs).every(i => i.value.trim() !== "");
    }
    if (step === 3) return document.querySelector('input[name="service"]:checked');
    if (step === 5) {
      if (!selectedDateStr) { alert("Please click a date on the calendar first."); return false; }
      return true;
    }
    return true;
  }

  document.getElementById("bookingForm").onsubmit = async function (e) {
    e.preventDefault();
    const btn = document.getElementById("modalSubmit");
    if (btn) {
      btn.innerText = "Processing...";
      btn.disabled = true;
    }
    const data = Object.fromEntries(new FormData(this).entries());
    console.log("Saving Data:", data);

    setTimeout(() => {
      document.querySelector("#bookingForm").innerHTML = `
        <div class="flex flex-col items-center justify-center h-full p-12 text-center">
          <div class="w-20 h-20 bg-blue-50 text-blue-600 rounded-full flex items-center justify-center text-4xl mb-6">✓</div>
          <h2 class="text-3xl font-bold text-slate-800 mb-2">Booking Success!</h2>
          <p class="text-slate-500">Redirecting to payment gateway...</p>
        </div>`;
      setTimeout(closeBookingModal, 3000);
    }, 1500);
  };
</script>"""

        content = content[:script_start] + script_new + content[script_end:]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Script successfully rewritten with logic merged!")
    else:
        print("Error: Could not find script block")


if __name__ == "__main__":
    main()
