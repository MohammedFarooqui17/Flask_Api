# <==================== ***** Function Based APi ***==========================================>



# from flask import Flask, jsonify, request
# import pymysql
# import json
# from decimal import Decimal

# app = Flask(__name__)

# def connection():
#     db = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='car', 
#     )
#     cur = db.cursor()
#     return cur, db
# cur,db = connection()


# @app.route('/api/carlist', methods=['GET', 'POST'])
# def car_list():
#     if request.method == 'GET':
#         try:
#             cur, db = connection()
#             query = "SELECT * FROM carlist"
#             cur.execute(query)
#             data = cur.fetchall()

#             car_list_data = []
#             discount_percentage = Decimal(10)  

#             for row in data:
#                 carlist = {
#                     "id": row[0],
#                     "name": row[1],
#                     "description": row[2],
#                     "activate": row[3],
#                     "chessinumber": row[4],
#                     "price": row[5]
#                 }
                
                
#                 discounted_price = carlist['price'] - (carlist['price'] * (discount_percentage / Decimal(100)))
#                 carlist['discounted_price'] = discounted_price
#                 car_list_data.append(carlist)

#             cur.close()
#             db.close()

#             return jsonify(car_list_data)

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

#     elif request.method == 'POST':
#         try:
#             data = request.get_json()
#             name = data.get('name')
#             description = data.get('description')
#             active = data.get('active', True)
#             chessinumber = data.get('chessinumber')
#             price = data.get("price")

#             if not name or not description:
#                 return jsonify({"error": "Name and description are required."}), 400

#             cur, db = connection()
#             query = "INSERT INTO carlist (name, descriptions, active, chessinumber, price) VALUES (%s, %s, %s, %s, %s)"
#             cur.execute(query, (name, description, active, chessinumber, price))
#             db.commit()

#             cur.close()
#             db.close()

#             return jsonify({"message": "Car added successfully!"}), 201

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500

#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# @app.route('/api/carlist/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
# def car_detail(pk):
#     if request.method == 'GET':
#         try:
#             cur, db = connection()
#             query = "SELECT * FROM carlist WHERE id=%s"
#             cur.execute(query, (pk,))
#             data = cur.fetchone()

#             if data:
#                 cardetail = {
#                     "id": data[0],
#                     "name": data[1],
#                     "descriptions": data[2],
#                     "activate": data[3],
#                     "chessinumber": data[4],
#                     "price": data[5]
#                 }
#                 cur.close()
#                 db.close()
#                 return jsonify(cardetail)
#             else:
#                 cur.close()
#                 db.close()
#                 return jsonify({"error": "Car not found."}), 404

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

#     elif request.method == 'PUT':
#         try:
#             data = request.get_json()
#             name = data.get('name')
#             descriptions = data.get('descriptions')
#             active = data.get('active', True)
#             chessinumber = data.get("chessinumber")
#             price = data.get("price")

#             if price is not None:
#                 try:
#                     price = float(price)
#                     if price < 50000:
#                         return jsonify({"error": "Price must be greater than fifty thousand."}), 400
#                 except ValueError:
#                     return jsonify({"error": "Invalid price value. It must be a number."}), 400
#             else:
#                 price = None

#             if not name or not descriptions:
#                 return jsonify({"error": "Name and description are required."}), 400

#             if active and (price is None or price < 0):
#                 return jsonify({"error": "If the car is active, price must be provided and cannot be negative."}), 400

#             if chessinumber and not isinstance(chessinumber, str):
#                 return jsonify({"error": "Chessinumber must be a string."}), 400

#             cur, db = connection()
#             query = "UPDATE carlist SET name=%s, descriptions=%s, active=%s, chessinumber=%s, price=%s WHERE id=%s"
#             cur.execute(query, (name, descriptions, active, chessinumber, price, pk))
#             db.commit()

#             cur.close()
#             db.close()

#             return jsonify({"message": "Car updated successfully!"})

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

#     elif request.method == 'DELETE':
#         try:
#             cur, db = connection()
#             query = "DELETE FROM carlist WHERE id=%s"
#             cur.execute(query, (pk,))
#             db.commit()

#             cur.close()
#             db.close()

#             return jsonify({"message": "Car deleted successfully!"})

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# if __name__ == '__app__':
#     app.run(debug=True)




# <==================== ***** Class Based APi ***==========================================>


# from flask import Flask, jsonify, request
# from flask.views import MethodView
# import pymysql
# import json
# from decimal import Decimal

# app = Flask(__name__)

# # Function to establish a connection to the database
# def connection():
#     db = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         database='car', 
#     )
#     cur = db.cursor()
#     return cur, db


# class CarList(MethodView):
    
#     def get(self):
#         try:
#             cur, db = connection()
#             query = "SELECT * FROM carlist"
#             cur.execute(query)
#             data = cur.fetchall()

#             car_list_data = []
#             discount_percentage = Decimal(10)  # Example: 10% discount

#             for row in data:
#                 carlist = {
#                     "id": row[0],
#                     "name": row[1],
#                     "description": row[2],
#                     "activate": row[3],
#                     "chessinumber": row[4],
#                     "price": row[5]
#                 }
                
#                 # Calculate the discounted price (10%)
#                 discounted_price = carlist['price'] - (carlist['price'] * (discount_percentage / Decimal(100)))
#                 carlist['discounted_price'] = discounted_price
#                 car_list_data.append(carlist)

#             cur.close()
#             db.close()

#             return jsonify(car_list_data)

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

#     def post(self):
#         try:
#             data = request.get_json()
#             name = data.get('name')
#             description = data.get('description')
#             active = data.get('active', True)
#             chessinumber = data.get('chessinumber')
#             price = data.get("price")

#             if not name or not description:
#                 return jsonify({"error": "Name and description are required."}), 400

#             cur, db = connection()
#             query = "INSERT INTO carlist (name, descriptions, active, chessinumber, price) VALUES (%s, %s, %s, %s, %s)"
#             cur.execute(query, (name, description, active, chessinumber, price))
#             db.commit()

#             cur.close()
#             db.close()

#             return jsonify({"message": "Car added successfully!"}), 201

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# class CarDetail(MethodView):
    
#     def get(self, pk):
#         try:
#             cur, db = connection()
#             query = "SELECT * FROM carlist WHERE id=%s"
#             cur.execute(query, (pk,))
#             data = cur.fetchone()

#             if data:
#                 cardetail = {
#                     "id": data[0],
#                     "name": data[1],
#                     "descriptions": data[2],
#                     "activate": data[3],
#                     "chessinumber": data[4],
#                     "price": data[5]
#                 }
#                 cur.close()
#                 db.close()
#                 return jsonify(cardetail)
#             else:
#                 cur.close()
#                 db.close()
#                 return jsonify({"error": "Car not found."}), 404

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

#     def put(self, pk):
#         try:
#             data = request.get_json()
#             name = data.get('name')
#             descriptions = data.get('descriptions')
#             active = data.get('active', True)
#             chessinumber = data.get("chessinumber")
#             price = data.get("price")

#             if price is not None:
#                 try:
#                     price = float(price)
#                     if price < 50000:
#                         return jsonify({"error": "Price must be greater than fifty thousand."}), 400
#                 except ValueError:
#                     return jsonify({"error": "Invalid price value. It must be a number."}), 400
#             else:
#                 price = None

#             if not name or not descriptions:
#                 return jsonify({"error": "Name and description are required."}), 400

#             if active and (price is None or price < 0):
#                 return jsonify({"error": "If the car is active, price must be provided and cannot be negative."}), 400

#             if chessinumber and not isinstance(chessinumber, str):
#                 return jsonify({"error": "Chessinumber must be a string."}), 400

#             cur, db = connection()
#             query = "UPDATE carlist SET name=%s, descriptions=%s, active=%s, chessinumber=%s, price=%s WHERE id=%s"
#             cur.execute(query, (name, descriptions, active, chessinumber, price, pk))
#             db.commit()

#             cur.close()
#             db.close()

#             return jsonify({"message": "Car updated successfully!"})

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

#     def delete(self, pk):
#         try:
#             cur, db = connection()
#             query = "DELETE FROM carlist WHERE id=%s"
#             cur.execute(query, (pk,))
#             db.commit()

#             cur.close()
#             db.close()

#             return jsonify({"message": "Car deleted successfully!"})

#         except pymysql.MySQLError as e:
#             return jsonify({"error": f"Database error: {str(e)}"}), 500
#         except Exception as e:
#             return jsonify({"error": f"Unexpected error: {str(e)}"}), 500


# # Register the views with the app
# app.add_url_rule('/api/carlist', view_func=CarList.as_view('car_list'))
# app.add_url_rule('/api/carlist/<int:pk>', view_func=CarDetail.as_view('car_detail'))


# if __name__ == '__app__':
#     app.run(debug=True)

