rule _Vx_Spanz_vribux
{
	meta:
		description = "Vx_ Spanz"
	strings:
		$a = {E800005E81EE????8D94????B41ACD21C784}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
