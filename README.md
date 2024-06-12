# Ball drop simulation
I created a ball falling simulation in 3D in python without using opengl.

# Explanation
After watching a Pixar Animation Studio movie, I wanted to create a 3D animation, so I surfed the Internet and found Pixar in the Box. During the lecture, it was interesting to learn that Pixar creates objects in movies using Pixar's 3D animation tools.

Unfortunately, the 3D animation tools used by Pixar were not made public. It's difficult to create good quality animation all at once, so to get started, I looked into how computers represent 3D objects.

After searching and studying, I learned that in order to express 3D objects on a computer, I had to study mathematics, physics, and algorithms. In high school, I had studied little physics and mathematics, so it was difficult to understand the equations, but as I searched for symbols one by one to understand the equations, I was able to successfully display 3D objects on the screen.

I was happy when I actually succeeded, but I couldn't shake the feeling that something was missing. So I decided to add animation. While thinking about what animation to add, the idea of ​​dropping a ball from above occurred to me.

When I created an animation by applying the free fall motion equation, I could see the screen moving with jerks. While looking for a way to express smoother movement, I found out that it was possible to extend Python to C/C++. Although I couldn't create smooth movements because I didn't have enough time to study, it was a project where I learned a lot.

Until now, in order to express 3D objects and their movements, you had to learn C++ or C#. Python is also possible, but it was difficult to express 3D objects. Now, you can easily express 3D objects and create animations with Python.

# Install and run
Step1. Download the source code and move to the project folder.

```
$ git clone https://github.com/winterjoker341/graphics-playtime.git
$ cd graphics-playtime/
```

Step2. Set up a python virtual environment and install the necessary packages.

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt  
```

Step3. Run the program.

```
$ python main.py
```

# Reference
* Graphic model
  * [Ray tracing](https://en.wikipedia.org/wiki/Ray_tracing_(graphics))
  * [Phong reflection model](https://en.wikipedia.org/wiki/Phong_reflection_model)

* Object Model
  * [Plane](https://en.wikipedia.org/wiki/Line%E2%80%93plane_intersection)
  * [Sphere](https://en.wikipedia.org/wiki/Line%E2%80%93sphere_intersection)

* Physics model
  * [Free fall](https://en.wikipedia.org/wiki/Free_fall)
  * [Inelastic collision](https://en.wikipedia.org/wiki/Inelastic_collision)

# License
[GNU LESSER GENERAL PUBLIC LICENSE](https://github.com/winterjoker341/graphics-playtime/blob/master/LICENSE)