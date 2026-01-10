# Eve Builds

This program is for corporate industry folks.  It does *not* look at prices.  It generates a list of materials to acquire from stores, or buy outright from a trade hub.

This program given a fit, and a quantity to build will generate a list of items to acquire from stores, or to buy outright from a trade hub.  Then it lists all the recipes you need to run, and how many runs of each recipe.

## "Fits" directory.

* This is a list of fits you build.
* Each file ends in ".fit" and is just the contents of "Copy to Clipboard" you get from the fittings window.
* One fit is openly listed as an example, you can run it directly (the .fit is not necessary).
* You have to manually manage the contents of this directory.

## non-researched directory.

* This is a list of all recipes (i.e. Blueprints) where the ingredients list are from a non researched blueprint.

## Recipes directory.

* Here are a list of recipes (i.e. Blueprints).
* You must manage this directory manually.
* A convenience script to copy the contents of the 'non-researched' directory to here is provided.
* Outside of the non researched blueprints, you should put in your researched blueprints to get accurate ingredient lists.
* In this context these recipes are a reduced list of items needed to run the recipe with a few other meta items.

An Example:

File recipes/"Hornet I".json
```
{
    "output" : 1,
    "type": "manufacture",
    "ingredients" : {
        "Tritanium" : 538,
        "Pyrite" : 60,
        "Isogen" : 4,
        "Noxcium" : 2
    }
}
```

The fields:

* 'output' - If you make 1 run of the recipe, this is how many of the item it will create.
* 'type' - Right now, it is not being used, but the choices are 'manufacture' and 'reaction'.
* 'ingredients' - These are the ingredients needed to make the run.

## Validating Recipes directory.

* After making changes to the recipes directory, you should run the program `validate_recipes.py` to make sure they are all syntactically correct and have all the required fields in them.

## Running the program.

So that you can see how it is intended to be run `run_test_fit.sh` shows the details.

Essentially `./build_list.py [path to fit file] [num of these fits]`.

Here is an example run, note I removed some of the debug elements of the program output.

```
==============================================================================
==============================================================================
==============================================================================

Ingredients List to build 10 fits/Armageddon: 4th Rate Linked.fit

Buy,'Arbalest' Rapid Heavy Missile Launcher I,50
Buy,100MN Monopropellant Enduring Afterburner,10
Buy,1600mm Steel Plates II,30
Buy,500MN Quad LiF Restrained Microwarpdrive,10
Buy,Armor Plates,1,660
Buy,Burned Logic Circuit,1,000
Buy,Caldari Navy Mjolnir Heavy Missile,12,000
Buy,Caldari Navy Vespa,50
Buy,Charred Micro Circuit,890
Buy,Contaminated Nanite Compound,1,120
Buy,Damage Control II,10
Buy,Explosive Coating II,10
Buy,Faint Epsilon Scoped Warp Scrambler,10
Buy,Fried Interface Control,1,660
Buy,Heavy F-RX Compact Capacitor Booster,10
Buy,Heavy Gremlin Compact Energy Neutralizer,20
Buy,Heavy Jigoro Enduring Stasis Grappler,10
Buy,Helium Fuel Blocks,125
Buy,Hydrogen Fuel Blocks,315
Buy,Large Armor Repairer II,10
Buy,Large I-ax Enduring Remote Armor Repairer,10
Buy,Multispectrum Coating II,10
Buy,Multispectrum Energized Membrane II,30
Buy,Navy Cap Booster 3200,50
Buy,Nitrogen Fuel Blocks,125
Buy,Oxygen Fuel Blocks,370
Buy,Parallel Enduring Target Painter,10
Buy,Thruster Console,330
Mineral,Isogen,1,307,540
Mineral,Megacyte,19,500
Mineral,Mexallon,3,913,090
Mineral,Nocxium,160,240
Mineral,Pyrite,26,129,780
Mineral,Tritanium,52,944,100
Mineral,Zydrine,45,440
Moon,Atmospheric Gases,30,800
Moon,Evaporite Deposits,8,800
Moon,Hydrocarbons,30,800
Moon,Silicates,8,800
P1,Chiral Structures,1,000
P1,Water,1,000
P2,Nanites,2,512
P2,Supertensile Plastics,2,000
P2,Test Cultures,2,000
P2,Viral Agent,2,000
P3,Data Chips,128
P3,Gel-Matrix Biopaste,128
P3,Guidance systems,30
P3,High-Tech Transmitters,30
P3,Nuclear Reactors,10
P3,Smartfab Units,30


Perform the Blueprint/Reaction Runs in this order:

Reaction Carbon Fiber Number of runs: 63
    Material Hydrocarbons 6300
    Material Evaporite Deposits 6300
    Material Hydrogen Fuel Blocks 315

Reaction Carbon Polymers Number of runs: 25
    Material Hydrocarbons 2500
    Material Silicates 2500
    Material Helium Fuel Blocks 125

Blueprint Core Probe Launcher I Number of runs: 10
    Material Tritanium 4710
    Material Pyrite 7160

Blueprint Core Scanner Probe I Number of runs: 240
    Material Tritanium 2640
    Material Pyrite 2880
    Material Mexallon 6720
    Material Isogen 2640
    Material Nocxium 960

Blueprint Hornet I Number of runs: 50
    Material Tritanium 26900
    Material Pyrite 3000
    Material Isogen 200
    Material Nocxium 100

Blueprint Inferno Heavy Missile Number of runs: 120
    Material Tritanium 85920
    Material Pyrite 240
    Material Mexallon 720
    Material Nocxium 360

Blueprint Large Higgs Anchor I Number of runs: 10
    Material Charred Micro Circuit 890
    Material Burned Logic Circuit 1000
    Material Thruster Console 330

Blueprint Large Trimark Armor Pump I Number of runs: 20
    Material Contaminated Nanite Compound 1120
    Material Fried Interface Control 1660
    Material Armor Plates 1660

Blueprint Mobile Depot Number of runs: 10
    Material Tritanium 55560
    Material Pyrite 2220
    Material Zydrine 4440
    Material Smartfab Units 30
    Material Nuclear Reactors 10
    Material Guidance systems 30
    Material High-Tech Transmitters 30

Blueprint Nanite Repair Paste Number of runs: 128
    Material Gel-Matrix Biopaste 128
    Material Nanites 512
    Material Data Chips 128

Blueprint Nova Heavy Missile Number of runs: 120
    Material Tritanium 42120
    Material Pyrite 14280
    Material Nocxium 120

Reaction Oxy-Organic Solvents Number of runs: 11
    Material Hydrocarbons 22000
    Material Atmospheric Gases 22000
    Material Oxygen Fuel Blocks 55

Reaction Sulfuric Acid Number of runs: 25
    Material Atmospheric Gases 2500
    Material Evaporite Deposits 2500
    Material Nitrogen Fuel Blocks 125

Reaction Thermosetting Polymer Number of runs: 63
    Material Atmospheric Gases 6300
    Material Silicates 6300
    Material Oxygen Fuel Blocks 315

Blueprint Vespa I Number of runs: 50
    Material Tritanium 131550
    Material Pyrite 27100
    Material Mexallon 5650
    Material Zydrine 200

Blueprint Wasp I Number of runs: 100
    Material Tritanium 594700
    Material Pyrite 72900
    Material Isogen 4700
    Material Nocxium 2700
    Material Zydrine 1800

Reaction Pressurized Oxidizers Number of runs: 25
    Reaction Carbon Polymers 5000
    Reaction Sulfuric Acid 5000
    Reaction Oxy-Organic Solvents 25

Blueprint Reinforced Carbon Fiber Number of runs: 63
    Reaction Carbon Fiber 12600
    Reaction Oxy-Organic Solvents 63
    Reaction Thermosetting Polymer 12600

Blueprint Auto-Integrity Preservation Seal Number of runs: 500
    Material Supertensile Plastics 2000
    Material Nanites 2000
    Blueprint Reinforced Carbon Fiber 5000

Blueprint Core Temperature Regulator Number of runs: 10
    Reaction Pressurized Oxidizers 5000
    Blueprint Reinforced Carbon Fiber 5000
    Material Chiral Structures 1000
    Material Water 1000

Blueprint Life Support Backup Unit Number of runs: 250
    Material Test Cultures 2000
    Material Viral Agent 2000
    Blueprint Reinforced Carbon Fiber 2500

Blueprint Armageddon Number of runs: 10
    Material Tritanium 52000000
    Material Pyrite 26000000
    Material Mexallon 3900000
    Material Isogen 1300000
    Material Nocxium 156000
    Material Zydrine 39000
    Material Megacyte 19500
    Blueprint Auto-Integrity Preservation Seal 1500
    Blueprint Core Temperature Regulator 10
    Blueprint Life Support Backup Unit 750

```

The first part of the output, is the list of items to acquire, the 2nd is each recipe (blueprint) to run and how many runs of each are needed.

