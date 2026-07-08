"""
responses.py

Class-specific scene text for Ex Umbris Fabricati.
Each scene key contains a response for every playable class.
"""

from core.text import say


CLASS_RESPONSES = {'assault_hive': {'Voidrunner': ['You are moving before the dust clears.',
                                 'The hive mouths, broken ridges, and kill lanes become a map only '
                                 'you can read.',
                                 'Where others see a swarm, you see a route through the '
                                 'impossible.'],
                  'Grimshield': ['You step forward and become the line.',
                                 'Claws crash against armor. Acid hisses across the ground.',
                                 'The squad gathers behind you because you make survival feel '
                                 'possible.'],
                  'Ashreaver': ['You answer the swarm with fire and thunder.',
                                'Every burst, grenade, and shell is delivered with sacred '
                                'violence.',
                                'The hive will not merely be defeated. It will be erased.'],
                  'Nightreaper': ['You vanish into smoke and motion.',
                                  'The first bugs fall before the swarm understands where death '
                                  'has entered.',
                                  'By the time they turn toward you, you are already elsewhere.'],
                  'Umbracaster': ['You read the swarm like a dark scripture.',
                                  'Patterns emerge in the chaos. Weaknesses reveal themselves.',
                                  'The shadows between each charge become a path.'],
                  'Ritesmith': ['You mark the hive node with practiced precision.',
                                'Charges are placed like ritual seals, each one part of a greater '
                                'design.',
                                'When the forge speaks, even the earth will remember.'],
                  'Oathkeeper': ['You mark the wounded first, pulling them from the killing ground '
                                 'before raising your weapon.',
                                 'Your vow is simple: none left behind.',
                                 'Only when your squad is steady do you turn your wrath toward the '
                                 'swarm.'],
                  'Fluxhunter': ['You feel the rhythm of the battlefield shifting beneath your '
                                 'boots.',
                                 'The swarm surges, splits, and reforms.',
                                 'One fracture in their pattern is all you need.'],
                  'Fumebinder': ['Smoke coils across the battlefield at your command.',
                                 'The swarm loses sight of your squad, but your squad does not '
                                 'lose sight of the objective.',
                                 'Confusion becomes cover. Cover becomes momentum.'],
                  'Emberbrand': ['You raise your weapon as fire blooms around the hive.',
                                 'The fear in your chest does not vanish. It burns.',
                                 'With every step forward, that ember becomes defiance.']},
 'search_outpost': {'Voidrunner': ['You kneel beside the tracks and trace the path of retreat '
                                   'through mud, ichor, and shattered stone.',
                                   'The signs are faint, but not lost to you.',
                                   'Someone survived long enough to leave a trail.'],
                    'Grimshield': ['You move through the ruins first.',
                                   'Every doorway becomes a threat. Every silence becomes a '
                                   'warning.',
                                   'Your squad follows because you make the broken place feel '
                                   'survivable.'],
                    'Ashreaver': ['You study the destruction with a practiced eye.',
                                  'This was not random slaughter. The bugs came in waves and '
                                  'dragged the rest below.',
                                  'Your grip tightens. Some ruins demand an answer.'],
                    'Nightreaper': ['You slip through the outpost like a shadow among dead lights.',
                                    'No movement. No breath. No sound except distant chittering '
                                    'beneath the floor.',
                                    'Then you find the markings.'],
                    'Umbracaster': ['You run gloved fingers across the scorched guild markings.',
                                    'There is memory here. Fear, resolve, and something left '
                                    'unfinished.',
                                    'The place feels less abandoned than waiting.'],
                    'Ritesmith': ['You recover a damaged beacon and crack open its casing.',
                                  'A few careful adjustments restore the ember-core by hand.',
                                  'The signal returns as a thin pulse in the dark.'],
                    'Oathkeeper': ['You kneel beside the remains and bow your head.',
                                   'Those who fall are not forgotten.',
                                   'Their names will be carried home, even if their bodies cannot '
                                   'be.'],
                    'Fluxhunter': ['Something about the outpost feels wrong.',
                                   'The damage pattern, the silence, the collapsed walls — all '
                                   'point to movement underground.',
                                   'This was not the end of an attack. It was the beginning of '
                                   'one.'],
                    'Fumebinder': ['You release a thin veil of smoke through the shattered '
                                   'corridors.',
                                   'Air currents reveal hidden cracks, collapsed tunnels, and one '
                                   'path beneath the rubble.',
                                   'The outpost still has secrets to give.'],
                    'Emberbrand': ['You find a half-burned banner beneath the debris.',
                                   'Its edge is blackened, but the mark of the Sanctum remains.',
                                   'You fold it carefully. Some flames deserve to be carried '
                                   'forward.']},
 'scout_ridge': {'Voidrunner': ['Your eyes move across the valley, measuring paths no map could '
                                'show.',
                                'Between craters, ridgelines, and broken rock, you find a route '
                                'for the squad.',
                                'The swarm owns the ground. You own the spaces between.'],
                 'Grimshield': ['You mark defensive positions before anyone else speaks.',
                                'High ground. Hard cover. Clean retreat lines.',
                                'If the swarm comes uphill, it will pay for every inch.'],
                 'Ashreaver': ['From the ridge, the hive network looks almost fragile.',
                               'Three tunnels. Three wounds in the earth.',
                               'You already know where the fire should fall.'],
                 'Nightreaper': ['You mark a silent path through the rocks.',
                                 'The swarm will not know you are there until the first tunnel '
                                 'burns.',
                                 'By then, it will be too late.'],
                 'Umbracaster': ['You watch the swarm until the chaos becomes language.',
                                 'The tunnels pulse in sequence, each one feeding the next.',
                                 'Destroy the rhythm, and the entire network stumbles.'],
                 'Ritesmith': ['You sketch firing lanes and demolition points into the dirt.',
                               'The ridge becomes more than a lookout.',
                               'It becomes the first line of a battlefield blueprint.'],
                 'Oathkeeper': ['Before choosing a target, you count your squad.',
                                'Breathing. Wounded. Shaken. Ready.',
                                'The mission matters, but the living matter more.'],
                 'Fluxhunter': ['You sense the rhythm of the swarm changing.',
                                'The attack has not fully begun. There is still time to break it.',
                                'Instability gathers near the western tunnel.'],
                 'Fumebinder': ['You call smoke across the ridge, veiling the squad from hostile '
                                'sight.',
                                'Under cover, the advance begins.',
                                'The enemy sees only haze where death is already moving.'],
                 'Emberbrand': ['The valley below crawls with impossible numbers.',
                                'Still, your resolve does not dim.',
                                'An ember does not ask how vast the dark is before it burns.']},
 'collapse_hive': {'Voidrunner': ['You lead the retreat route before the detonator is armed.',
                                  'Every squadmate knows exactly where to run when the tunnels '
                                  'ignite.'],
                   'Grimshield': ['You remain nearest the blast zone until the last member clears '
                                  'the tunnel mouth.',
                                  'Only then do you fall back.'],
                   'Ashreaver': ['You smile beneath your helmet.',
                                 'This is the work you were made for.'],
                   'Nightreaper': ['You place the final charge in silence.',
                                   'No wasted motion. No hesitation. Just an ending waiting to '
                                   'happen.'],
                   'Umbracaster': ['You feel the pressure shift beneath the soil as if the planet '
                                   'itself is inhaling.',
                                   'The hive knows what is coming.'],
                   'Ritesmith': ['Your placement is exact, each charge part of a pattern only you '
                                 'fully understand.',
                                 'Destruction, when properly shaped, becomes craft.'],
                   'Oathkeeper': ['You wait until every squadmate confirms distance before giving '
                                  'the signal.',
                                  'Victory means nothing if the living are abandoned to earn it.'],
                   'Fluxhunter': ['The tunnel network pulses with instability.',
                                  'You trigger the collapse at the exact moment the swarm '
                                  'overcommits.'],
                   'Fumebinder': ['You flood the tunnel mouth with smoke before the retreat.',
                                  'The swarm charges blind into its own grave.'],
                   'Emberbrand': ['You watch the detonator light turn green.',
                                  'A single spark is all it takes to bury a kingdom of monsters.']},
 'recover_beacon': {'Voidrunner': ["You recognize the route encoded in the beacon's last "
                                   'transmission.',
                                   'Whoever carried it was trying to lead others home.'],
                    'Grimshield': ['You cradle the beacon behind your armor plate as if shielding '
                                   'another survivor.',
                                   'Even damaged signals deserve protection.'],
                    'Ashreaver': ['The beacon is scarred by acid and flame.',
                                  'You wonder how many bugs paid for each inch it was carried.'],
                    'Nightreaper': ['You retrieve the beacon without disturbing the nest around '
                                    'it.',
                                    'Some memories must be stolen back from the dark.'],
                    'Umbracaster': ['The broken signal carries more than coordinates.',
                                    'There are fragments of fear, duty, and one final warning.'],
                    'Ritesmith': ['You open the casing and coax the signal back to life.',
                                  'The machine coughs, sparks, then remembers its purpose.'],
                    'Oathkeeper': ['You hold the beacon carefully, as if it were a wounded thing.',
                                   'Names deserve more than silence.'],
                    'Fluxhunter': ['The transmission is unstable, but not random.',
                                   'You isolate the pattern and recover the final coordinates.'],
                    'Fumebinder': ['You conceal the recovery beneath a curtain of smoke.',
                                   'By the time the swarm notices, the beacon is already in '
                                   'Sanctum hands.'],
                    'Emberbrand': ['The beacon flickers in your palm like a stubborn coal.',
                                   'Against all odds, something still burns.']},
 'line_hold': {'Voidrunner': ['You move between weak points faster than the swarm can exploit '
                              'them.',
                              'Every gap closes a breath before disaster arrives.'],
               'Grimshield': ['Every step backward is measured. Every stand is deliberate.',
                              'You do not hold because victory is certain. You hold because others '
                              'need time.'],
               'Ashreaver': ['You turn the approach into a killing field.',
                             'If the swarm wants the line, it must crawl through ruin first.'],
               'Nightreaper': ['You move along the edge of chaos, cutting down anything that slips '
                               'through.',
                               'Your squad hears the bugs fall before they see you strike.'],
               'Umbracaster': ["You watch the swarm's pressure points and call targets with cold "
                               'precision.',
                               'The line survives because the chaos is no longer unreadable.'],
               'Ritesmith': ['You repair a jammed emplacement under fire.',
                             'The turret roars back to life like a forge given breath.'],
               'Oathkeeper': ['You drag one soldier back by the armor strap and shove a stim into '
                              'his hand.',
                              'Not here. Not today.'],
               'Fluxhunter': ['You sense the breach before it forms.',
                              'Your warning shifts the squad just enough to survive the next '
                              'surge.'],
               'Fumebinder': ['Smoke and dust roll across the kill zone, turning panic into '
                              'controlled confusion.',
                              'The swarm charges blind into prepared fire.'],
               'Emberbrand': ['You keep shouting even when your throat burns.',
                              'As long as one voice carries, the line still lives.']},
 'save_seaf': {'Voidrunner': ['You plot the fastest route through shell craters and unstable '
                              'ground.',
                              'Seconds matter. You intend to steal as many as you can.'],
               'Grimshield': ['You check your armor, roll your shoulders, and move toward the '
                              'failing line.',
                              'Someone needs a wall. You are already on your way.'],
               'Ashreaver': ['The distant gunfire sharpens your focus.',
                             'Whatever is hunting those soldiers is about to learn what wrath '
                             'looks like.'],
               'Nightreaper': ['You lower your profile and vanish into the broken terrain.',
                               'If the SEAF are trapped, the swarm will never see their rescue '
                               'coming.'],
               'Umbracaster': ['You read the friendly signals like fading candles in the dark.',
                               'Each one still burning is a reason to move faster.'],
               'Ritesmith': ['You mark supply routes, ammunition needs, and possible extraction '
                             'points at once.',
                             'Saving soldiers requires more than courage. It requires structure.'],
               'Oathkeeper': ['The moment you see the friendly signals, your path is chosen.',
                              'A vow is not spoken only when survival is convenient.'],
               'Fluxhunter': ['The firefight ahead is unstable and worsening.',
                              'You can feel the moment approaching when rescue becomes '
                              'impossible.'],
               'Fumebinder': ['You prepare smoke cover before the squad even reaches the ridge.',
                              'A rescue under open sky is just a massacre waiting for a veil.'],
               'Emberbrand': ['The distant gunfire sounds almost like a heartbeat.',
                              'Weak, desperate, but still alive.']},
 'bad_ending': {'Voidrunner': ['You bought them the seconds they needed.',
                               'The path home exists because you carved it with your final '
                               'charge.'],
                'Grimshield': ['You became the shield one last time.',
                               'The line endured because you refused to fall back.'],
                'Ashreaver': ["Your final act was ruin delivered at arm's length.",
                              'The Charger fell with you in the fire.'],
                'Nightreaper': ['The enemy never saw the final strike coming.',
                                'Your shadow passed over the battlefield and left silence behind.'],
                'Umbracaster': ['Your last warning carried through broken comms and static.',
                                'Those who survived did so because you read the darkness '
                                'correctly.'],
                'Ritesmith': ["Your final act became part of the battlefield's design.",
                              'A sacrifice shaped into survival for others.'],
                'Oathkeeper': ['The SEAF survivors live because you chose the vow over the self.',
                               'No ally was abandoned while breath remained.'],
                'Fluxhunter': ['You saw the collapse coming and stepped into it anyway.',
                               'The fracture closed around you, but others escaped through it.'],
                'Fumebinder': ['Smoke covered the survivors until the last possible second.',
                               'When it cleared, your sacrifice was already legend.'],
                'Emberbrand': ['Your final act becomes a flame others gather around.',
                               'The ember does not die. It is passed on.']},
 'set_base': {'Voidrunner': ['You map approach routes, fallback paths, and emergency exits.',
                             'A base is only safe if its people can move when the ground turns '
                             'against them.'],
              'Grimshield': ['You place defenses where the line is most likely to break.',
                             'If the swarm comes again, it will meet preparation instead of '
                             'panic.'],
              'Ashreaver': ['You turn choke points into future graves.',
                            'Every mine, turret, and firing lane promises the swarm a violent '
                            'welcome.'],
              'Nightreaper': ['You mark blind spots and shadowed angles around the perimeter.',
                              'Anything trying to slip through will find you waiting.'],
              'Umbracaster': ['You study the land and the silence beneath it.',
                              'The base feels temporary. The danger beneath it does not.'],
              'Ritesmith': ['You turn chaos into structure with practiced hands.',
                            'Beacon placement, supply lanes, turret angles — each decision becomes '
                            'part of the forge.'],
              'Oathkeeper': ['You establish a triage point before anything else.',
                             'Walls matter. Weapons matter. But the wounded must have somewhere to '
                             'return.'],
              'Fluxhunter': ['You mark unstable ground and shifting patrol patterns around the '
                             'perimeter.',
                             'Something is coming. You intend to know from where.'],
              'Fumebinder': ['You map the wind, smoke drift, and choke points.',
                             'By nightfall, the base will be wrapped in confusion only your squad '
                             'understands.'],
              'Emberbrand': ['You place a small marker near the center of camp.',
                             'A reminder that even on hostile ground, the flame can take root.']},
 'continue_scout': {'Voidrunner': ['The terrain speaks in small signs: broken soil, shifted '
                                   'stones, distant movement.',
                                   'You follow the quiet warnings others would miss.'],
                    'Grimshield': ['You scout with one eye on the horizon and one on your squad.',
                                   'Information matters, but nobody gets left exposed.'],
                    'Ashreaver': ['You track the patrol by the damage it leaves behind.',
                                  'Broken earth. Split chitin. Trails of acid. Soon, it will leave '
                                  'nothing at all.'],
                    'Nightreaper': ['You keep low and silent, crossing the scarred terrain without '
                                    'disturbing loose stone.',
                                    'Even your squad has to check twice to know where you are.'],
                    'Umbracaster': ['You study the silence between distant howls.',
                                    'There is a pattern beneath the noise, and it is growing '
                                    'closer.'],
                    'Ritesmith': ['You mark the ground as you move, building a mental map of '
                                  'future fortifications.',
                                  'Even a scouting path can become a supply line.'],
                    'Oathkeeper': ['You keep the pace steady, checking breathing, ammunition, and '
                                   'morale.',
                                   'A tired squad makes mistakes. A watched squad survives.'],
                    'Fluxhunter': ['The battlefield feels unstable, as if the ground itself is '
                                   'holding back a scream.',
                                   'You are not scouting for patrols anymore. You are hunting the '
                                   'source of the shift.'],
                    'Fumebinder': ['You test the air and watch the way dust rolls over the ridge.',
                                   'The wind will either betray you or save you. You intend to '
                                   'make it save you.'],
                    'Emberbrand': ['You move through the scarred land with stubborn resolve.',
                                   'Every step forward is proof that fear has not won.']},
 'fourth_choice': {'Voidrunner': ['Your mind races through routes, angles, distances.',
                                  'There is no perfect path, only the one that keeps people '
                                  'alive.'],
                   'Grimshield': ['You feel the old instinct rise: get between the monster and '
                                  'everyone else.',
                                  'Even against a Titan, the shield answers.'],
                   'Ashreaver': ['The sight of it does not freeze you.',
                                 'It gives your fury a shape.'],
                   'Nightreaper': ['Against something that large, silence feels impossible.',
                                   'Still, you search for the blind spot. Everything has one.'],
                   'Umbracaster': ['For a heartbeat, the shadow beneath it seems larger than the '
                                   'creature itself.',
                                   'You feel the battlefield tilt around its presence.'],
                   'Ritesmith': ['Your eyes snap to tools, weapons, machines, possibilities.',
                                 'The answer is not courage alone. The answer is hardware.'],
                   'Oathkeeper': ['You glance first to the wounded, then to the Titan.',
                                  'The choice is cruel, but the vow remains clear.'],
                   'Fluxhunter': ["The entire field destabilizes around the Titan's arrival.",
                                  'You feel the battle tipping toward disaster.'],
                   'Fumebinder': ['You watch the Titan through dust and fumes.',
                                  'If the squad survives this, it will be because the beast never '
                                  'sees clearly.'],
                   'Emberbrand': ['Something inside you flares despite the terror.',
                                  'The bigger the darkness, the brighter the flame must become.']},
 'load_mech': {'Voidrunner': ['The cockpit seals around you, and every movement becomes speed '
                              'magnified by steel.',
                              'For once, the fastest route is straight through.'],
               'Grimshield': ['The mech is not just a weapon. It is a walking fortress.',
                              'And for this moment, that fortress is yours.'],
               'Ashreaver': ['The weapons spin hot, and you feel the old joy of destruction settle '
                             'into focus.',
                             'The Titan has made itself a target.'],
               'Nightreaper': ['A mech is louder than your usual work, but subtlety has its '
                               'limits.',
                               'Sometimes death announces itself.'],
               'Umbracaster': ['The targeting system paints the Titan in cold light.',
                               'For a moment, machine logic and shadowed instinct become one.'],
               'Ritesmith': ['The machine answers your hands like a familiar tool.',
                             'Steel, pressure, recoil, heat — everything has a language.'],
               'Oathkeeper': ['You bring the mech between the Titan and the wounded.',
                              'This is not glory. This is protection at scale.'],
               'Fluxhunter': ['You feel the recoil, the sway, the unstable pressure in the ground '
                              'beneath it.',
                              'You fire at the exact moment the Titan overextends.'],
               'Fumebinder': ['Smoke rolls around the mech as you advance.',
                              'The Titan sees a silhouette. You see a target.'],
               'Emberbrand': ['Warning lights flash around you like sparks in a furnace.',
                              'You grin as the cockpit becomes a shrine to controlled fire.']},
 'run_cover': {'Voidrunner': ["You move fast, drawing the Titan's attention away from the mech "
                              'just long enough.',
                              'Speed becomes bait. Bait becomes survival.'],
               'Grimshield': ['You hate leaving the machine to another, but the line needs more '
                              'than pride.',
                              'You cover the approach and make sure your squadmate reaches it '
                              'alive.'],
               'Ashreaver': ['You dive into cover and open fire immediately.',
                             'If someone else has the bigger gun, you will make sure they get to '
                             'use it.'],
               'Nightreaper': ['You disappear into cover and begin cutting down smaller threats '
                               'around the mech.',
                               'The Titan is not the only danger on the field.'],
               'Umbracaster': ['You read the battlefield and choose the wiser path.',
                               'Power unused is not weakness when it is placed in the right '
                               'hands.'],
               'Ritesmith': ["You ping the mech, then cover the pilot's approach with disciplined "
                             'fire.',
                             'A tool serves best in the hands closest to it.'],
               'Oathkeeper': ['Trust is also a vow.',
                              'You do not need to be the one in the machine to keep your squad '
                              'alive.'],
               'Fluxhunter': ['You saw the better path a second before pride could blind you.',
                              'The right choice is not always the glorious one.'],
               'Fumebinder': ['You throw smoke across the approach, giving your squadmate the '
                              'seconds needed to reach the cockpit.',
                              'The Titan roars at shadows while steel wakes behind the veil.'],
               'Emberbrand': ['You duck into cover and keep firing.',
                              'Not every flame must be the largest to keep the dark at bay.']}}


def class_response(player, scene_key):
    """Print the class-specific response for the current scene."""
    class_name = player.class_name

    try:
        lines = CLASS_RESPONSES[scene_key][class_name]
    except KeyError as error:
        raise KeyError(f"Missing class response for scene={scene_key!r}, class={class_name!r}") from error

    for line in lines:
        say(line)
