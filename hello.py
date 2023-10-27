from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World! OI mundão</p>"

@app.route("/products")
def products():
    response = jsonify([

        {"title":" Caneca Personalizada de Porcelanato - Backend",
         "amount":123.45,
         "installments":{"number":3,"total": 41.15, "hasFee": True},
         },

        {"title":" Caneca de Tulipa - Backend",
         "amount":123.45,
         "installments":{"number":3,"total": 41.15},
         },
       
       {"title":" Caneca de Barro - Backend",
         "amount":123.45,
         "installments":{"number":3,"total": 41.15},
         },

         {"title":" Caneca de Ouro - Backend",
         "amount":123.45,
         "installments":{"number":3,"total": 41.15},
         },


    ])

    response.headers.add('Access-Control-Allow-Origin','*')
    return response




if __name__ == '__main__':
    app.run(debug=True,port=5000)