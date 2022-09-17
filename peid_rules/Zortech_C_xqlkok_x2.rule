rule _Zortech_C_xqlkok
{
	meta:
		description = "Zortech C"
	strings:
		$a = {FAFCB8??????8CC88ED8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
