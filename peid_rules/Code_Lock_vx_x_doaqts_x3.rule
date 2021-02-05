rule _Code_Lock_vx_x_doaqts
{
	meta:
		description = "Code_Lock vx_x"
	strings:
		$a = {478BC2051E00528BD0B8023DCD218BD85A}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
