shader_type canvas_item;
// from https://www.youtube.com/watch?v=nyFzPaWAzeQ
uniform float rate = 1.0;

void vertex() {
	if(VERTEX.x > 0.0){
		VERTEX += vec2(-sin(UV.x + TIME*2.0),sin(UV.y + TIME*2.0))*10.0;
	}
}


