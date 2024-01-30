Typescript: supertest, static Checking javascript code compile

If we want to use it we need to write npx tsc "file.name"

Data Types: 
            Number - String - Boolean
            Null -  undefined - void
            Object - Array - Tuples - ....
            Any -  Never - Unknown
            npm i --save-dev @type/node


-npx tsc -v

*Transform into js or compile

-npx tsc filename.ts

npx tsc --init
    :permite configurar tsc

configuracion determinadas
    npx tsc --init --rootDir build 
    --esModuleInterop --resolveJsonModule --lib es6 --module commonjs 

tsconfig.json

"exclude": ["/path","folder"]