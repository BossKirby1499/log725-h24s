shader_type canvas_item;
// from https://www.youtube.com/watch?v=nyFzPaWAzeQ
uniform float rate = 1.0;

void vertex() {
	VERTEX += vec2(-sin(VERTEX.x + TIME*2.0),sin(VERTEX.y + TIME*2.0))*10.0;
}


