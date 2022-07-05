from dbOperations import initialiseDB
from dbOperations import incrimentDBRecord
from dbConnection import mySQLConnect

from flask import Flask
from flask import jsonify




def configure_routes(app):
    
    @app.route('/count', methods=['GET'])
    def counter():
        response = incrimentDBRecord()
        return str(response), 200

    @app.route("/healthz", methods=['GET'])
    def healthz():
            mydb = mySQLConnect()
            dbUp = mydb.is_connected()
            if dbUp:
                #return {"db_healthy": "true"}, 200
                return jsonify({"db_healthy":"true"}),200
            else:
                #return {"db_healthy": "false"}, 500
                return jsonify({"db_healthy":"false"}),500

    @app.route('/dummy', methods=['GET'])
    def dummy():
        return "success", 200


app = Flask(__name__)
configure_routes(app)

initialiseDB()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


