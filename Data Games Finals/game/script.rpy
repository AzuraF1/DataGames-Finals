# Declare characters used by this game.
define e = Character("Eileen")

# Initialize score variables
default score = 0
default total_possible = 34 

label start:
    $ score = 0
    scene bg room 
    show eileen happy
    
    e "Welcome to the Data Games Finals: The Cretaceous Period!"
    
    # --------------------------------------------------
    # PART 1: Narrative & Quiz
    # --------------------------------------------------
    e "Part 1: Beginning of a New Period"
    e "The Jurassic Period, hailed as the 'golden age of dinosaurs,' was a time when these reptiles roamed the Earth."
    e "So, how did these dominant creatures die out, although it may be a bit murky? Fossil records do tell us that there was significant fauna turnover, with the emergence of diverse new species and the decline of others."
    e "Such as the Stegosaurus, which went extinct in North America but continued in Europe."
    e "The Jurassic didn’t end with a dramatic extinction event but with a slow transition into the Cretaceous Period."
    e "In geological time, it was the last and longest period of the Mesozoic Era and Phanerozoic Eon. Which started from 145 million years ago and ended 66 million years ago."
    
    e "What do you think is the most well-known about the Cretaceous Period?"
    menu:
        "Dinosaurs":
            $ score += 1
        "Plants":
            $ score += 1
        "Reptiles":
            $ score += 1
        "The extinction event":
            $ score += 1
            
    e "Actually, all of those are correct. This period featured diverse reptiles and dinosaurs. As well as the first ever watering of plants, and the death of all dinosaurs."
    
    e "The name Cretaceous is derived from the Latin word creta, which means 'chalk', and was proposed by J.B.J Omalious d’Halloy in 1822."
    
    e "So what was life like back then? The Earth used to be a single landmass, a supercontinent called..."
    menu:
        "Pangea":
            e "That's correct, it was called Pangea, which was surrounded by a vast sea called Panthalassa."
            $ score += 1
        "Laurasia":
            e "Well, that’s incorrect; it was called the Pangea, which was surrounded by a vast sea called Panthalassa."
        "Gondowana":
            e "Well, that’s incorrect; it was called the Pangea, which was surrounded by a vast sea called Panthalassa."
        "Panthalassa":
            e "Well, that’s incorrect; it was called the Pangea, which was surrounded by a vast sea called Panthalassa."

    e "By the time the Cretaceous rolled around, it split into two: The northern half is called Laurasia, and the southern half is called Gondwana, both separated by the Tethys Sea."
    e "As the continents shifted apart, it moved closer to the position that it is today."
    e "The climate was much warmer, and there was little to no ice in the North or South Pole. Additionally, the sea levels were much higher by 170 meters than what it is today."
    e "Shallow seas divided continents; for example, the Western Interior Seaway split North America into two landmasses."
    e "The largest was more than 3,000 kilometres long, almost 1,000 kilometres wide, and 760 metres deep."
    e "The Cretaceous is split into two parts called epochs."
    e "The early epoch lasted from 145 to 100.5 million years ago. While the late epoch lasted from 100.5 to 66 million years ago."

    e "It's time for the Part 1 Quiz!"

    e "1. What are the southern and northern supercontinents called?"
    menu:
        "A. Gondwana and Laurasia":
            $ score += 1
            e "Correct!"
        "B. Gondwona and Laurasia":
            e "Incorrect."
        "C. Gondwono and Laurosia":
            e "Incorrect."
        "D. Gondwana and Lourasia":
            e "Incorrect."

    e "2. Who proposed the name for Cretaceous?"
    menu:
        "A. J.B.J Omolious d’Holloy":
            e "Incorrect."
        "B. J.B.J Omolious d’Halloy":
            e "Incorrect."
        "C. J.J.J Omalious d’Halloy":
            e "Incorrect."
        "D. J.B.J Omalious d’Halloy":
            $ score += 1
            e "Correct!"

    e "3. What does Cretaceous mean?"
    menu:
        "A. Chalk":
            $ score += 1
            e "Correct!"
        "B. Fossil":
            e "Incorrect."
        "C. Dinosaur":
            e "Incorrect."
        "D. Reptile":
            e "Incorrect."

    e "4. What is the supercontinent called?"
    menu:
        "A. Gondowoland":
            e "Incorrect."
        "B. Panthalassa":
            e "Incorrect."
        "C. Pangea":
            $ score += 1
            e "Correct!"
        "D. Laurasia":
            e "Incorrect."

    e "5. What period is considered the “Golden Age of Dinosaurs”?"
    menu:
        "A. Cretaceous Period":
            e "Incorrect."
        "B. Mesozoic Period":
            e "Incorrect."
        "C. Triassic Period":
            e "Incorrect."
        "D. Jurassic Period":
            $ score += 1
            e "Correct!"

    e "6. When did the Cretaceous start?"
    menu:
        "A. 145 million Years Ago":
            $ score += 1
            e "Correct!"
        "B. 140 million Years Ago":
            e "Incorrect."
        "C. 150 million Years Ago":
            e "Incorrect."
        "D. 100 million Years Ago":
            e "Incorrect."

    e "7. How long did the Cretaceous Period last?"
    menu:
        "A. 79 million Years":
            $ score += 1
            e "Correct!"
        "B. 80 Million Years":
            e "Incorrect."
        "C. 100 Million Years":
            e "Incorrect."
        "D. 68 Million Years":
            e "Incorrect."

    e "8. What caused the Jurassic Period to transition to the Cretaceous Period?"
    menu:
        "A. Global Warming":
            e "Incorrect."
        "B. Fauna Turnover":
            $ score += 1
            e "Correct!"
        "C. Asteroid":
            e "Incorrect."
        "D. World Freezing":
            e "Incorrect."

    e "9. What is the ocean that surrounded Pangea called?"
    menu:
        "A. Phantalassa":
            $ score += 1
            e "Correct!"
        "B. Tethys Sea":
            e "Incorrect."
        "C. Shallow Sea":
            e "Incorrect."
        "D. Western Sea":
            e "Incorrect."

    e "10. Longest period of the Mesozoic Era?"
    menu:
        "A. Phanezoic Period":
            e "Incorrect."
        "B. Triassic Period":
            e "Incorrect."
        "C. Jurassic Period":
            e "Incorrect."
        "D. Cretaceous Period":
            $ score += 1
            e "Correct!"

    # --------------------------------------------------
    # PART 2: Narrative & Quiz
    # --------------------------------------------------
    e "Part 2: Plant Life and Dinosaurs"
    e "Plant life in the Cretaceous was different from what it is today. Since there was barely any ice in the Cretaceous, rainforests were able to grow near the poles."
    e "But unlike the rainforest in North America’s Pacific Northwest, each winter the Cretaceous polar forest would have had to survive four months of the year living in the total darkness of polar night."
    e "Today, 90%% of plants are flowering plants, known as angiosperms. The origin of flowering plants goes back as far as the Triassic Period."
    e "Though there was not much evidence of them at the start of the Cretaceous period. But by the end of the period, angiosperms are the most prominent part."
    e "Insect pollination happens earlier on in the Jurassic with gymnosperms which is a group of seed-producing plants, but it becomes much bigger with the flowering plants."
    e "Most of the insects are just as big as the dinosaurs in this period. But why is that?"
    e "There were theories that suggest the abundance of food and CO2. While others suggest the evolutionary arms races, where prey grew larger to avoid predators, forcing predators to grow larger in turn."
    e "Since big prey animals couldn’t run they had to find other ways to defend themselves. Such as the largest recorded dinosaur, the Titanosaurus, which belonged to a group of Sauropod dinosaurs."

    e "Let’s go over the major group of dinosaurs in this period."
    e "Theropods are carnivorous dinosaurs of a group whose members were typically bipedal and ranged from small and delicately built to very large."
    e "They are also characterized by hollow bones and three toes and claws on each limb. This group includes the famous Tyrannosaurids such as the Tyrannosaurus, Tarbosaurus, Albertosaurus and Dromaesaurids."
    e "Ornithischians are mainly herbivorous dinosaurs characterized by a pelvic structure superficially similar to that of birds. The name Ornithischia, or 'bird-hipped' has several distinct groups."
    e "Ceratopsians, such as Triceratops, are known for their horns, parrot-like beaks, and large frills at the back of their skulls, which may have been used for protection or display."
    e "Hadrosaurs, also called 'duck-billed dinosaurs,' include Edmontosaurus and Shantungosaurus, and were known for their flat snouts and ability to chew tough plant material."
    e "Ankylosaurs, like Ankylosaurus and Saichania, were heavily armored dinosaurs with bony plates and often a clubbed tail used for defense."
    e "Pachycephalosaurs, such as Pachycephalosaurus and Stegoceras, are recognized for their thick, dome-shaped skulls, which may have been used in head-butting behavior."
    e "Sauropods are characterized by having very long necks, long tails, small heads, and four thick, pillar-like legs. They are notable for the enormous sizes attained by some species."

    e "It's time for the Part 2 Quiz!"

    e "1. Why were rainforests able to grow near the poles during the Cretaceous period?"
    menu:
        "A. Because of volcanic activity":
            e "Incorrect."
        "B. Because there was little to no ice":
            $ score += 1
            e "Correct!"
        "C. Because of human influence":
            e "Incorrect."
        "D. Because of low oxygen levels":
            e "Incorrect."

    e "2. What challenge did polar forests face during the Cretaceous period?"
    menu:
        "A. Extreme heat":
            e "Incorrect."
        "B. Lack of rainfall":
            e "Incorrect."
        "C. Four months of total darkness":
            $ score += 1
            e "Correct!"
        "D. Constant flooding":
            e "Incorrect."

    e "3. What are flowering plants also known as?"
    menu:
        "A. Gymnosperms":
            e "Incorrect."
        "B. Bryophytes":
            e "Incorrect."
        "C. Angiosperms":
            $ score += 1
            e "Correct!"
        "D. Ferns":
            e "Incorrect."

    e "4. When did flowering plants begin to become dominant?"
    menu:
        "A. Beginning of the Jurassic":
            e "Incorrect."
        "B. End of the Cretaceous":
            $ score += 1
            e "Correct!"
        "C. Middle of the Triassic":
            e "Incorrect."
        "D. End of the Jurassic":
            e "Incorrect."

    e "5. What type of plants were first involved in insect pollination during the Jurassic?"
    menu:
        "A. Angiosperms":
            e "Incorrect."
        "B. Gymnosperms":
            $ score += 1
            e "Correct!"
        "C. Mosses":
            e "Incorrect."
        "D. Ferns":
            e "Incorrect."

    e "6. What is one theory explaining why many organisms grew very large during this time?"
    menu:
        "A. Lack of predators":
            e "Incorrect."
        "B. Decrease in oxygen":
            e "Incorrect."
        "C. Abundance of food and CO2":
            $ score += 1
            e "Correct!"
        "D. Limited space":
            e "Incorrect."

    e "7. Which group of dinosaurs were primarily carnivorous and walked on two legs?"
    menu:
        "A. Sauropods":
            e "Incorrect."
        "B. Ornithischians":
            e "Incorrect."
        "C. Theropods":
            $ score += 1
            e "Correct!"
        "D. Ankylosaurs":
            e "Incorrect."

    e "8. What is a key characteristic of Ornithischian dinosaurs?"
    menu:
        "A. Hollow bones":
            e "Incorrect."
        "B. Bird-like pelvic structure":
            $ score += 1
            e "Correct!"
        "C. Ability to fly":
            e "Incorrect."
        "D. Sharp claws for hunting":
            e "Incorrect."

    e "9. Which group of dinosaurs is known for having heavy armor and clubbed tails?"
    menu:
        "A. Hadrosaurs":
            e "Incorrect."
        "B. Ceratopsians":
            e "Incorrect."
        "C. Ankylosaurs":
            $ score += 1
            e "Correct!"
        "D. Pachycephalosaurs":
            e "Incorrect."

    e "10. What are Sauropods best known for?"
    menu:
        "A. Flying ability":
            e "Incorrect."
        "B. Sharp teeth":
            e "Incorrect."
        "C. Long necks and massive size":
            $ score += 1
            e "Correct!"
        "D. Dome-shaped skulls":
            e "Incorrect."


    # --------------------------------------------------
    # PART 3: Narrative & Quiz
    # --------------------------------------------------
    e "Part 3: The End of an Era"
    e "The end of the Cretaceous Period is marked by one of the most important events in Earth’s history—the Cretaceous–Paleogene extinction event."
    e "This event happened around 66 million years ago and caused the extinction of about 75%% of all species on Earth, including all non-avian dinosaurs."
    e "But what exactly caused this mass extinction?"
    e "Scientists believe that a massive asteroid struck the Earth near present-day Mexico, forming the Chicxulub Crater."
    e "This impact released an enormous amount of energy, far greater than millions of nuclear bombs."
    e "As a result, it caused huge wildfires to spread across the land, massive tsunamis to form in the oceans, and dust and debris to be thrown into the atmosphere."
    e "This debris blocked sunlight, causing darkness that lasted for months or even years."
    e "Without sunlight, plants could not perform photosynthesis, leading to the collapse of food chains."

    e "So, what happened when sunlight was blocked?"
    menu:
        "Plants grew faster":
            e "That’s incorrect; blocking sunlight caused plants to die and disrupted the entire food chain."
        "Food chains collapsed":
            e "That’s correct, without sunlight, plants die, and food chains collapse."
            $ score += 1
        "Oceans disappeared":
            e "That’s incorrect; blocking sunlight caused plants to die and disrupted the entire food chain."
        "Dinosaurs became stronger":
            e "That’s incorrect; blocking sunlight caused plants to die and disrupted the entire food chain."

    e "In addition to the asteroid impact, scientists also suggest that volcanic activity may have contributed to the extinction."
    e "Large volcanic eruptions released gases that changed the climate, making conditions even more difficult for life to survive."

    e "So, what are the two main factors believed to have caused the extinction?"
    menu:
        "Earthquakes and floods":
            e "Not quite, the extinction was mainly caused by an asteroid impact along with volcanic activity."
        "Asteroid impact and volcanic activity":
            e "Correct, both an asteroid impact and volcanic activity contributed to the extinction."
            $ score += 1
        "Disease and predators":
            e "Not quite, the extinction was mainly caused by an asteroid impact along with volcanic activity."
        "Ice age and storms":
            e "Not quite, the extinction was mainly caused by an asteroid impact along with volcanic activity."

    e "Despite this massive extinction, not all life disappeared."
    e "Some animals survived, including: Small mammals, Birds (which are descendants of dinosaurs), Reptiles, and amphibians."
    e "These surviving species later evolved and adapted to the new environment."

    e "So, which group survived and later became dominant?"
    menu:
        "Dinosaurs":
            e "That’s incorrect; mammals were among the survivors and later became dominant."
        "Mammals":
            e "That’s right, mammals survived and later became dominant."
            $ score += 1
        "Marine reptiles":
            e "That’s incorrect; mammals were among the survivors and later became dominant."
        "Ammonites":
            e "That’s incorrect; mammals were among the survivors and later became dominant."

    e "It's time for the final Quiz!"

    e "1. What major event marked the end of the Cretaceous Period?"
    menu:
        "A. Ice Age":
            e "Incorrect."
        "B. Cretaceous–Paleogene extinction event":
            $ score += 1
            e "Correct!"
        "C. Industrial Revolution":
            e "Incorrect."
        "D. Formation of continents":
            e "Incorrect."

    e "2. Approximately how many species became extinct during this event?"
    menu:
        "A. 25%%":
            e "Incorrect."
        "B. 50%%":
            e "Incorrect."
        "C. 75%%":
            $ score += 1
            e "Correct!"
        "D. 90%%":
            e "Incorrect."

    e "3. What was the main cause of the mass extinction according to scientists?"
    menu:
        "A. Flooding":
            e "Incorrect."
        "B. Disease":
            e "Incorrect."
        "C. Asteroid impact":
            $ score += 1
            e "Correct!"
        "D. Human activity":
            e "Incorrect."

    e "4. Where did the asteroid strike the Earth?"
    menu:
        "A. Africa":
            e "Incorrect."
        "B. Antarctica":
            e "Incorrect."
        "C. Present-day Mexico":
            $ score += 1
            e "Correct!"
        "D. Europe":
            e "Incorrect."

    e "5. What was the name of the crater formed by the asteroid impact?"
    menu:
        "A. Vredefort Crater":
            e "Incorrect."
        "B. Chicxulub Crater":
            $ score += 1
            e "Correct!"
        "C. Barringer Crater":
            e "Incorrect."
        "D. Sudbury Basin":
            e "Incorrect."

    e "6. What happened when dust and debris blocked sunlight?"
    menu:
        "A. Plants grew faster":
            e "Incorrect."
        "B. Food chains collapsed":
            $ score += 1
            e "Correct!"
        "C. Oceans disappeared":
            e "Incorrect."
        "D. Dinosaurs became stronger":
            e "Incorrect."

    e "7. What environmental effects were caused by the asteroid impact?"
    menu:
        "A. Snowstorms and earthquakes only":
            e "Incorrect."
        "B. Wildfires, tsunamis, and atmospheric dust":
            $ score += 1
            e "Correct!"
        "C. Strong winds only":
            e "Incorrect."
        "D. Heavy rainfall only":
            e "Incorrect."

    e "8. What additional factors may have contributed to the extinction?"
    menu:
        "A. Tornadoes":
            e "Incorrect."
        "B. Volcanic activity":
            $ score += 1
            e "Correct!"
        "C. Ocean currents":
            e "Incorrect."
        "D. Solar flares":
            e "Incorrect."

    e "9. What did volcanic eruptions release that affected the climate?"
    menu:
        "A. Water vapor only":
            e "Incorrect."
        "B. Oxygen":
            e "Incorrect."
        "C. Gases":
            $ score += 1
            e "Correct!"
        "D. Sand":
            e "Incorrect."

    e "10. Which group survived and later became dominant after the extinction?"
    menu:
        "A. Dinosaurs":
            e "Incorrect."
        "B. Mammals":
            $ score += 1
            e "Correct!"
        "C. Marine reptiles":
            e "Incorrect."
        "D. Ammonites":
            e "Incorrect."


    # --------------------------------------------------
    # FINAL RESULTS
    # --------------------------------------------------
    e "You have completed the entire lesson!"
    e "Let's look at your final score..."
    
    e "You scored [score] out of [total_possible]."
    
    if score >= 30:
        e "Incredible work! You are a true Paleontology master!"
    elif score >= 20:
        e "Great job! You know quite a bit about the Cretaceous period."
    elif score >= 10:
        e "Not bad, but there's still plenty to learn about the Mesozoic era."
    else:
        e "Oof. You might want to replay and review the material!"

    # This ends the game.
    return