//Incrementa automaticamente

enum values {
    value0 = 0,
    value1,
    value2,
    value3,
    value4
}

const getValue = values.value0;


enum Estados {
    "completado" = "C",
    "Incompleto" = "I",
    "Pendiente" = "P"
}

let estadosTareas: Estados = Estados.Incompleto;