rule _EXE_joiner__Amok_jwtwzq
{
	meta:
		description = "EXE joiner __ Amok"
	strings:
		$a = {A114A14000C1E002A318A140}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
