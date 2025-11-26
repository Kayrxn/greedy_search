needed_states = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
added_states = set(["nm", "tx", "ok", "ks", "co", "ne", "sd", "wy", "nd", "ia", "mn", "mo", "ar", "la"])
needed_states.update(added_states)

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])
stations["ksix"] = set(["nm", "tx", "ok"])
stations["kseven"] = set(["ok", "ks", "co"])
stations["keight"] = set(["ks", "co", "ne"])
stations["knine"] = set(["ne", "sd", "wy"])
stations["kten"] = set(["nd", "ia"])
stations["keleven"] = set(["mn", "mo", "ar"])
stations["ktwelve"] = set(["la"])
stations["kthirteen"] = set(["mo", "ar"])

def greedy_search(needed, stations):
    covered = set()    # estados ya cubiertos hasta ahora
    selected = []    # lista de estaciones seleccionadas

    stations = stations.copy()  # para no modificar el original

    while covered != needed:  # mientras no cubramos todos los estados
        best_station = None  # mejor estación en esta vuelta
        new_states = set()   # estados nuevos que cubriría la mejor estación

        for station, states in stations.items():  # recorremos todas las estaciones disponibles
            added = states - covered  # estados que esta estación añadiría
            if len(added) > len(new_states):  # si cubre más que la mejor hasta ahora
                new_states = added
                best_station = station

        if best_station is None:  # no hay estación restante
            break

        selected.append(best_station)  # añadimos la estación seleccionada
        covered |= new_states          # añadimos los estados nuevos a los cubiertos
        del stations[best_station]     # eliminamos la estación para no volver a usarla

    return selected, covered

result_stations, result_covered = greedy_search(needed_states, stations)
print("Selected stations:", result_stations)
print("Covered states:", result_covered)