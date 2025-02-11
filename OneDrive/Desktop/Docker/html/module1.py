from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todo_list = []  # In-memory storage for to-do items

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            todo_list.append(task)
        return redirect(url_for("index"))  # Redirect to prevent form resubmission

    return render_template("index.html", todo_list=todo_list)

@app.route("/delete/<int:index>")  # Route for deleting tasks
def delete(index):
    if 0 <= index < len(todo_list):  # Check if index is valid
        del todo_list[index]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)  # debug=True for easier development
