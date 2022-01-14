#version 130

struct Material {
  sampler2D diffuse;
  vec3 specular;
  float shininess;
};

struct Light {
  vec3 position;
  vec3 ambient;
  vec3 diffuse;
  vec3 specular;
};

out vec4 frag_col;

in vec3 frag_3Dpos;
in vec3 vs_normal;
in vec2 TexCoords;

uniform Material material;
uniform Light light;
uniform Light light2;
uniform vec3 view_pos;

void main() {

  // Ambient -> light
  vec3 ambient = light.ambient * vec3(texture(material.diffuse, TexCoords));
  // Ambient -> light2
  vec3 ambient2 = light2.ambient * vec3(texture(material.diffuse, TexCoords));

  // Diffuse -> light
  vec3 light_dir = normalize(light.position - frag_3Dpos);
  // Diffuse -> light2
  vec3 light2_dir = normalize(light2.position - frag_3Dpos);
  
  // Calculo del producto vectorial del vector luz y la normal
  // En funcion del angulo dara positivo, 0 o negativo
  // En funcion del resultado se sabe si incide la luz o no
  float diff = max(dot(vs_normal , light_dir), 0.0);  
  vec3 diffuse = light.diffuse * diff * vec3(texture(material.diffuse, TexCoords));  

  float diff2 = max(dot(vs_normal , light2_dir), 0.0);
  vec3 diffuse2 = light2.diffuse * diff2 * vec3(texture(material.diffuse, TexCoords));  

  // Specular
  vec3 view_dir = normalize(view_pos - frag_3Dpos);
  // light
  vec3 reflect_dir = reflect(-light_dir, vs_normal);
  float spec = pow(max(dot(view_dir, reflect_dir), 0.0), material.shininess);
  vec3 specular = light.specular * (spec * material.specular);

  // light 2
  vec3 reflect_dir2 = reflect(-light2_dir, vs_normal);
  float spec2 = pow(max(dot(view_dir, reflect_dir2), 0.0), material.shininess);
  vec3 specular2 = light2.specular * (spec2 * material.specular);

  vec3 result = ambient + ambient2 + diffuse + diffuse2 + specular + specular2;
  
  frag_col = vec4(result, 1.0);
}
