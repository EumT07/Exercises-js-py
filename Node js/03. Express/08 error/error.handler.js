function logError(err, req, res, next) {
    console.error(err);
    next(err);
};

function errorHandler(err, req, res, next) {
    res.status(500).json({
        message: error.message,
        stack: err.stack
    });
}

module.exports = {logError, errorHandler};


//Para el uso, debe ir despues de las rutas en el archivo principal de la app.

//Manejo de errores con Boom libreria
