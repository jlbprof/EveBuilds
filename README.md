# Eve Builds

This program is for corporate industry folks.  I does *not* look at prices.  It generates a list of materials to acquire from stores, or buy outright from a trade hub.

This program given a fit, and a quantity to build will generate a list of items to acquire from stores, or to buy outright from a trade hub.  Then it lists all the recipes you need to run, and how many runs of each recipe.

## "Fits" directory.

* This is a list of fits you build.
* Each file ends in ".fit" and is just the contents of "Copy to Clipboard" you get from the fittings window.
* One fit is openly listed as an example, you can run it directly (the .fit is not necessary).
* You have to manually managed the contents of this directory.

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

Ingredients List to build 10 fits/Armageddon: Test Fit.fit.examples

Buy,'Arbalest' Rapid Heavy Missile Launcher I,5
Buy,100MN Monopropellant Enduring Afterburner,1
Buy,1600mm Steel Plates II,3
Buy,500MN Quad LiF Restrained Microwarpdrive,1
Buy,Armor Plates,166
Buy,Burned Logic Circuit,100
Buy,Caldari Navy Mjolnir Heavy Missile,1,200
Buy,Caldari Navy Vespa,5
Buy,Charred Micro Circuit,89
Buy,Contaminated Nanite Compound,112
Buy,Damage Control II,1
Buy,Explosive Coating II,1
Buy,Faint Epsilon Scoped Warp Scrambler,1
Buy,Fried Interface Control,166
Buy,Heavy F-RX Compact Capacitor Booster,1
Buy,Heavy Gremlin Compact Energy Neutralizer,2
Buy,Heavy Jigoro Enduring Stasis Grappler,1
Buy,Helium Fuel Blocks,125
Buy,Hydrogen Fuel Blocks,315
Buy,Large Armor Repairer II,1
Buy,Large I-ax Enduring Remote Armor Repairer,1
Buy,Multispectrum Coating II,1
Buy,Multispectrum Energized Membrane II,3
Buy,Navy Cap Booster 3200,5
Buy,Nitrogen Fuel Blocks,125
Buy,Nocxium,270
Buy,Oxygen Fuel Blocks,370
Buy,Parallel Enduring Target Painter,1
Buy,Thruster Console,33
Mineral,Isogen,1,300,754
Mineral,Megacyte,19,500
Mineral,Mexallon,3,901,309
Mineral,Noxcium,156,154
Mineral,Pyrite,26,012,978
Mineral,Tritanium,52,094,410
Mineral,Zydrine,39,644
Moon,Atmospheric Gases,30,800
Moon,Evaporite Deposits,8,800
Moon,Hydrocarbons,30,800
Moon,Silicates,8,800
P1,Chiral Structures,1,000
P1,Water,1,000
P2,Nanites,2,052
P2,Supertensile Plastics,2,000
P2,Test Cultures,2,000
P2,Viral Agent,2,000
P3,Data Chips,13
P3,Gel-Matrix Biopaste,13
P3,Guidance systems,3
P3,High-Tech Transmitters,3
P3,Nuclear Reactors,1
P3,Smartfab Units,3

Runs needed for each recipe
Armageddon 10
Auto-Integrity Preservation Seal 500
Carbon Fiber 63
Carbon Polymers 25
Core Probe Launcher I 1
Core Scanner Probe I 24
Core Temperature Regulator 10
Hornet I 5
Inferno Heavy Missile 12
Large Higgs Anchor I 1
Large Trimark Armor Pump I 2
Life Support Backup Unit 250
Mobile Depot 1
Nanite Repair Paste 13
Nova Heavy Missile 12
Oxy-Organic Solvents 11
Pressurized Oxidizers 25
Reinforced Carbon Fiber 63
Sulfuric Acid 25
Thermosetting Polymer 63
Vespa I 5
Wasp I 10
```

The first part of the output, is the list of items to acquire, the 2nd is each recipe (blueprint) to run and how many runs of each are needed.

