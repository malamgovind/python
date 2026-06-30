| Tool         | Use                  |
| ------------ | -------------------- |
| print()      | Check Variables      |
| breakpoint() | Pause Program        |
| pdb          | Interactive Debugger |
| assert       | Validate Condition   |
| logging      | Debug in Production  |






```text
===========================================
             37_debugging.py
        COMPLETE THEORY DIAGRAM
===========================================

DEBUGGING
│
├── Definition
│   │
│   ├── Process of Finding Bugs
│   │      → Program માં રહેલી Bugs (ભૂલો) શોધવાની પ્રક્રિયા.
│   │
│   ├── Analyze Bugs
│   │      → Bug કેમ આવ્યો, ક્યાં આવ્યો અને તેનું મૂળ કારણ શું છે તે તપાસવું.
│   │
│   ├── Fix Bugs
│   │      → Bug ને યોગ્ય Logic અથવા Code દ્વારા સુધારવો.
│   │
│   └── Verify Program
│          → Fix કર્યા પછી Program ફરી ચલાવી ખાતરી કરવી કે Bug દૂર થયો છે.
│
├── Purpose
│   │
│   ├── Detect Errors
│   │      → Program માં રહેલી તમામ પ્રકારની Errors શોધવી.
│   │
│   ├── Understand Problems
│   │      → Error પાછળનું સાચું કારણ સમજીને તેનું વિશ્લેષણ કરવું.
│   │
│   ├── Improve Code Quality
│   │      → Code ને વધુ Clean, Readable અને Maintainable બનાવવો.
│   │
│   ├── Improve Performance
│   │      → Unnecessary Operations દૂર કરીને Program ને ઝડપી બનાવવો.
│   │
│   ├── Increase Reliability
│   │      → Software ને વધુ Stable અને વિશ્વસનીય બનાવવું.
│   │
│   └── Produce Correct Output
│          → દરેક Input માટે યોગ્ય અને Expected Output મેળવવો.
│
├── Software Development Life Cycle
│   │
│   ├── Requirement
│   │      → User ની જરૂરિયાતો અને Project ની Requirements એકત્રિત કરવી.
│   │
│   ├── Design
│   │      → Software ની Structure, Architecture અને Logic તૈયાર કરવું.
│   │
│   ├── Coding
│   │      → Design મુજબ Actual Program લખવો.
│   │
│   ├── Testing
│   │      → Program યોગ્ય રીતે કામ કરે છે કે નહીં તેની ચકાસણી કરવી.
│   │
│   ├── Debugging
│   │      → Testing દરમિયાન મળેલી Bugs શોધીને Fix કરવી.
│   │
│   ├── Deployment
│   │      → તૈયાર થયેલ Software ને User સુધી પહોંચાડવું.
│   │
│   └── Maintenance
│          → Release પછી નવા Updates, Improvements અને Bug Fixes કરવાં.
│
├── Program Execution
│   │
│   ├── Source Code
│   │      → Developer દ્વારા લખાયેલ Python Program.
│   │
│   ├── Python Interpreter
│   │      → Source Code ને વાંચીને Execute કરતું Software.
│   │
│   ├── Execute Program
│   │      → Interpreter Program ચલાવવાનું શરૂ કરે છે.
│   │
│   ├── Error?
│   │     │
│   │     ├── Yes
│   │     │     ├── Debug
│   │     │     │      → Error શોધીને Analyze કરવી.
│   │     │     │
│   │     │     ├── Fix
│   │     │     │      → Error દૂર કરવા માટે Code સુધારવો.
│   │     │     │
│   │     │     └── Run Again
│   │     │            → સુધારેલ Program ફરી Execute કરવો.
│   │     │
│   │     └── No
│   │            └── Correct Output
│   │                   → Program સફળતાપૂર્વક યોગ્ય Output આપે છે.
│   │
│   └── Program Ends
│          → Execution સફળતાપૂર્વક પૂર્ણ થાય છે.
│
├── Types of Errors
│   │
│   ├── Syntax Error
│   │     ├── Grammar Mistake
│   │     │      → Python ના Grammar Rules નો ભંગ થવો.
│   │     │
│   │     ├── Detected Before Execution
│   │     │      → Interpreter Program ચલાવતાં પહેલાં શોધી લે છે.
│   │     │
│   │     └── Program Doesn't Start
│   │            → Syntax Error હોય તો Program Run થતો નથી.
│   │
│   ├── Runtime Error
│   │     ├── Occurs During Execution
│   │     │      → Program ચાલતી વખતે Error થાય છે.
│   │     │
│   │     ├── Raises Exception
│   │     │      → Runtime દરમિયાન Exception Generate થાય છે.
│   │     │
│   │     └── Program May Stop
│   │            → ગંભીર Error હોય તો Program અટકી શકે છે.
│   │
│   ├── Logical Error
│   │     ├── Program Runs
│   │     │      → Program કોઈ Error વગર Execute થાય છે.
│   │     │
│   │     ├── No Exception
│   │     │      → Interpreter કોઈ Exception બતાવતો નથી.
│   │     │
│   │     └── Wrong Output
│   │            → Logic ખોટો હોવાથી Result ખોટો મળે છે.
│   │
│   └── Semantic Error
│         ├── Syntax Correct
│         │      → Program ની Syntax સંપૂર્ણ સાચી હોય છે.
│         │
│         ├── Meaning Wrong
│         │      → Code નો અર્થ અથવા ઉપયોગ ખોટો હોય છે.
│         │
│         └── Unexpected Behaviour
│                → Program Expected પ્રમાણે વર્તન કરતો નથી.
```
```text
├── Debugging Process
│   │
│   ├── Detect Problem
│   │      → સૌથી પહેલા Program માં સમસ્યા ક્યાં છે તે ઓળખવી.
│   │
│   ├── Reproduce Problem
│   │      → Bug ને ફરીથી ઉભો કરીને તેનું વર્તન સમજવું.
│   │
│   ├── Observe Behaviour
│   │      → Program કેવી રીતે કામ કરે છે તે ધ્યાનથી જોવું.
│   │
│   ├── Locate Bug
│   │      → Bug કઈ Line અથવા Function માં છે તે શોધવું.
│   │
│   ├── Analyze Cause
│   │      → Bug પાછળનું મૂળ કારણ (Root Cause) શોધવું.
│   │
│   ├── Fix Code
│   │      → જરૂરી ફેરફાર કરીને Bug દૂર કરવો.
│   │
│   ├── Test Again
│   │      → Fix પછી Program ફરી ચલાવી Test કરવો.
│   │
│   └── Verify Result
│          → ખાતરી કરવી કે Bug સંપૂર્ણ દૂર થયો છે.
│
├── Debugger
│   │
│   ├── Execute Line by Line
│   │      → Program ને એક-એક Line પ્રમાણે Execute કરાવે છે.
│   │
│   ├── Pause Execution
│   │      → જરૂર પડે ત્યાં Program ને રોકી શકાય છે.
│   │
│   ├── Inspect Variables
│   │      → Variables ની Current Value જોઈ શકાય છે.
│   │
│   ├── Inspect Objects
│   │      → Memory માં રહેલા Objects ની સ્થિતિ તપાસી શકાય છે.
│   │
│   ├── Inspect Memory
│   │      → Memory Allocation અને References જોઈ શકાય છે.
│   │
│   ├── Inspect Call Stack
│   │      → Function Calls નો ક્રમ જોઈ શકાય છે.
│   │
│   └── Resume Execution
│          → Pause પછી Program ફરી Continue થાય છે.
│
├── Breakpoint
│   │
│   ├── Stop Execution
│   │      → ચોક્કસ Line પર Program અટકાવવામાં આવે છે.
│   │
│   ├── Inspect State
│   │      → Program ની હાલની સ્થિતિ તપાસી શકાય છે.
│   │
│   ├── Analyze Variables
│   │      → Variables ની Values ચકાસી શકાય છે.
│   │
│   └── Continue Execution
│          → તપાસ પૂર્ણ થયા પછી Program આગળ વધે છે.
│
├── Step Execution
│   │
│   ├── Step Into
│   │     └── Function ની અંદર જઈ દરેક Line Execute કરે છે.
│   │
│   ├── Step Over
│   │     └── Function ને અંદર ગયા વગર Execute કરે છે.
│   │
│   └── Step Out
│         └── હાલની Function માંથી બહાર આવી Caller પર પાછું આવે છે.
│
├── Variable Inspection
│   │
│   ├── Variable Name
│   │      → Variable નું નામ ઓળખવા માટે.
│   │
│   ├── Variable Value
│   │      → Variable માં રહેલી હાલની Value જોવા માટે.
│   │
│   ├── Data Type
│   │      → Variable કયા Type નો છે તે જાણવા.
│   │
│   ├── Reference
│   │      → Variable કયા Object ને Point કરે છે તે જાણવા.
│   │
│   └── Current State
│          → Execution દરમિયાન Variable ની હાલની સ્થિતિ જોવા.
│
├── Memory Inspection
│   │
│   ├── Stack Memory
│   │     ├── Local Variables
│   │     │      → Function ના Local Variables અહીં Store થાય છે.
│   │     │
│   │     ├── Function Calls
│   │     │      → દરેક Function Call માટે Stack Frame બને છે.
│   │     │
│   │     └── References
│   │            → Temporary References Stack માં રહે છે.
│   │
│   └── Heap Memory
│         ├── Objects
│         │      → Python Objects Heap માં Store થાય છે.
│         │
│         ├── Lists
│         │      → List Objects Heap Memory માં રહે છે.
│         │
│         ├── Dictionaries
│         │      → Dictionary Objects Heap માં Store થાય છે.
│         │
│         ├── Sets
│         │      → Set Objects Heap Memory નો ઉપયોગ કરે છે.
│         │
│         └── Class Objects
│                → Class ના Instances Heap માં Create થાય છે.
│
├── Call Stack
│   │
│   ├── main()
│   │      → Program નું શરૂઆતનું Function.
│   │
│   ├── function()
│   │      → main() દ્વારા Call થયેલી Function.
│   │
│   ├── another_function()
│   │      → આગળ Call થયેલી Function.
│   │
│   └── current_function()
│          → હાલમાં Execute થતી Function.
│
├── Watch Window
│   │
│   ├── Monitor Variables
│   │      → પસંદ કરેલા Variables પર સતત નજર રાખે છે.
│   │
│   ├── Live Updates
│   │      → Value બદલાય એટલે તરત Update થાય છે.
│   │
│   └── Value Tracking
│          → Variable ની Value માં થતા ફેરફારો Track કરે છે.
│
├── Print Debugging
│   │
│   ├── print()
│   │      → Variable અથવા Message Console માં Print કરવું.
│   │
│   ├── Console Output
│   │      → Print થયેલી માહિતી Console માં દેખાય છે.
│   │
│   ├── Manual Analysis
│   │      → Developer જાતે Output જોઈને Bug શોધે છે.
│   │
│   └── Beginner Friendly
│          → શરૂઆતના Developers માટે સૌથી સરળ રીત.
│
├── Logging
│   │
│   ├── Record Messages
│   │      → Program ની માહિતી Log File માં સાચવે છે.
│   │
│   ├── Runtime Information
│   │      → Execution દરમિયાનની માહિતી Record કરે છે.
│   │
│   ├── Production Environment
│   │      → Live Applications માં Logging વધુ ઉપયોગી છે.
│   │
│   └── Error History
│          → જૂના Errors નો Record સાચવી રાખે છે.
│
├── Common Bug Causes
│   │
│   ├── Wrong Logic
│   │      → Algorithm અથવા Logic ખોટો હોવો.
│   │
│   ├── Wrong Variable
│   │      → ખોટો Variable ઉપયોગ કરવો.
│   │
│   ├── Invalid Input
│   │      → User દ્વારા ખોટો Input મળવો.
│   │
│   ├── Wrong Condition
│   │      → if/else Condition ખોટી લખવી.
│   │
│   ├── Wrong Loop
│   │      → Loop ની Condition અથવા Logic ખોટી હોવી.
│   │
│   ├── Wrong Function Call
│   │      → Function ને ખોટી રીતે Call કરવી.
│   │
│   ├── Missing Validation
│   │      → Input અથવા Data Validate ન કરવું.
│   │
│   └── Memory Problems
│          → Memory Management સંબંધિત સમસ્યાઓ.
│
├── Best Practices
│   │
│   ├── Reproduce Bug
│   │      → Bug ફરી ઉભો કરી સમજી લેવો.
│   │
│   ├── Understand Root Cause
│   │      → મૂળ કારણ શોધીને Fix કરવું.
│   │
│   ├── Fix One Bug At A Time
│   │      → એક સમયે એક Bug જ Fix કરવો.
│   │
│   ├── Test Again
│   │      → દરેક Fix પછી Testing કરવી.
│   │
│   ├── Use Debugger
│   │      → Professional Debugging Tools નો ઉપયોગ કરવો.
│   │
│   ├── Use Logging
│   │      → Errors નો Record રાખવો.
│   │
│   ├── Write Clean Code
│   │      → સરળ અને વાંચી શકાય એવો Code લખવો.
│   │
│   └── Review Code
│          → Code Review દ્વારા Bugs ઘટાડવા.
│
├── Advantages
│   │
│   ├── Better Code Quality
│   │      → Code વધુ વિશ્વસનીય બને છે.
│   │
│   ├── Easy Maintenance
│   │      → ભવિષ્યમાં ફેરફાર કરવો સરળ બને છે.
│   │
│   ├── Faster Development
│   │      → Bugs ઝડપથી દૂર થતા Development ઝડપે થાય છે.
│   │
│   ├── Reliable Software
│   │      → Software વધુ Stable બને છે.
│   │
│   ├── Better Performance
│   │      → Performance Problems શોધી શકાય છે.
│   │
│   └── Easier Problem Solving
│          → સમસ્યાઓ ઝડપથી સમજી અને ઉકેલી શકાય છે.
│
├── Disadvantages
│   │
│   ├── Time Consuming
│   │      → મોટા Bugs શોધવામાં વધુ સમય લાગે છે.
│   │
│   ├── Difficult In Large Projects
│   │      → મોટા Projects માં Debugging મુશ્કેલ બને છે.
│   │
│   ├── Logical Bugs Hard To Find
│   │      → Logical Errors સૌથી મુશ્કેલ હોય છે.
│   │
│   └── Requires Experience
│          → અસરકારક Debugging માટે અનુભવ જરૂરી છે.
│
├── Real World Usage
│   │
│  ├── Web Applications
│   │      → Websites અને Web APIs Debug કરવા.
│   │
│  ├── Desktop Software
│   │      → Desktop Programs ની સમસ્યાઓ શોધવા.
│   │
│  ├── Mobile Apps
│   │      → Android અને iOS Apps Debug કરવા.
│   │
│  ├── Games
│   │      → Game Logic અને Performance સુધારવા.
│   │
│  ├── Machine Learning
│   │      → Model અને Data Pipeline ની Errors શોધવા.
│   │
│  ├── Data Science
│   │      → Data Processing Bugs શોધવા.
│   │
│  ├── Automation
│   │      → Automation Scripts ની સમસ્યાઓ દૂર કરવા.
│   │
│  └── Embedded Systems
│          → Hardware સાથે જોડાયેલા Programs Debug કરવા.
│
└── Final Goal
    │
    ├── Bug Free Code
    │      → શક્ય તેટલો Error-Free Program બનાવવો.
    │
    ├── Correct Output
    │      → દરેક Input માટે સાચું Result આપવું.
    │
    ├── Stable Program
    │      → Program Crash વગર સતત ચાલે.
    │
    ├── High Performance
    │      → ઓછા Resources સાથે ઝડપથી કામ કરે.
    │
    ├── Easy Maintenance
    │      → ભવિષ્યમાં Update અને Fix કરવું સરળ બને.
    │
    └── Better User Experience
           → User ને વિશ્વસનીય અને સરળ Software મળે.
```
