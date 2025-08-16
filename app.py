from flask import Flask, jsonify, request

app = Flask(__name__)  # Inicializa la aplicación Flask

tasks = [
    {"id": 1, "title": "Aprender Github", "done": False},
    {"id": 2, "title": "Aprender Docker", "done": False},
    {"id": 3, "title": "Aprender Kubernetes", "done": False},
    {"id": 4, "title": "Aprender Python", "done": False},
    {"id": 5, "title": "Aprender Flask", "done": False},
] # Lista para almacenar las tareas

#GET: Listar todas las tareas
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

#GET: Obtener una tarea por ID
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Tarea no encontrada"}), 404
    return jsonify(task)

#POST: Crear una nueva tarea
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Título de la tarea es requerido"}), 400
    new_task = {
        "id": len(tasks) + 1,
        "title": data['title'],
        "done": False
    }
    tasks.appends(new_task)
    return jsonify(new_task), 201

#PUT: Actualizar una tarea por ID
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404
    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['done'] = data.get('done', task['done'])
    return jsonify(task)

#DELETE: Eliminar una tarea por ID
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Tarea eliminada"}), 204

if __name__ == '__main__':  # Ejecuta la aplicación Flask
    app.run(debug=True, host='0.0.0.0', port=8080)  # Permite que la aplicación sea accesible desde cualquier IP en el puerto 5000