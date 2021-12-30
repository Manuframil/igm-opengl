/*
  A surface normal for a triangle can be calculated by taking the vector cross
  product of two edges of that triangle. The order of the vertices used in the 
  calculation will affect the direction of the normal (in or out of the face 
  w.r.t. winding).

  So for a triangle p1, p2, p3, if the vector U = p2 - p1 and the vector 
  V = p3 - p1 then the normal N = U X V and can be calculated by:

  Nx = UyVz - UzVy

  Ny = UzVx - UxVz

  Nz = UxVy - UyVx

 Given that a vector is a structure composed of three floating point numbers and
 a Triangle is a structure composed of three Vectors, based on the above definitions
 */
glm::vec3 calcularNormal(glm::vec3 p1, glm::vec3 p2, glm::vec3 p3){
  glm::vec3 U = p2 - p1;
  glm::vec3 V = p3 - p1;

  float normalX = U[1] * V[2] - U[2] * V[1];
  float normalY = U[2] * V[0] - U[0] * V[2];
  float normalZ = U[0] * V[1] - U[1] * V[0];

  glm::vec3 normal(normalX, normalY, normalZ);

  return normal;
}

GLfloat * calcularNormalesCubo(GLfloat cubo[]){
  
  GLfloat normales[] = {};
  
  for(int i = 0; i<105; i+=9){
    glm::vec3 normal = calcularNormal(cubo[i], cubo[i+1], cubo[i+2]);
    normales[i] = normal[0];
    normales[i+1] = normal[1];
    normales[i+2] = normal[2];
  }

  return normales;
}