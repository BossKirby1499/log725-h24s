shader_type canvas_item;

uniform float rate = 1.0;

void fragment() {
    vec4 color = vec4(0.0, 1.0, 1., 1.0); 
    vec4 original_color = texture(TEXTURE, UV);
    vec4 green_color = original_color * color;
	float progression = sin(TIME*1.5);
	if(UV.x > 0.0 && UV.x < progression){
		COLOR = green_color;
	}
}
void vertex() {
	VERTEX += vec2(-sin(VERTEX.x + TIME*2.0),sin(VERTEX.y + TIME*2.0))*10.0;
}