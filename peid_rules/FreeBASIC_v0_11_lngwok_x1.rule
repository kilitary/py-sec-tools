rule _FreeBASIC_v0_11_lngwok
{
	meta:
		description = "FreeBASIC v0_11"
	strings:
		$a = {E8????0000E801000000C35589E5}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
