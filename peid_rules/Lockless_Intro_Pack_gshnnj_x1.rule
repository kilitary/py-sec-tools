rule _Lockless_Intro_Pack_gshnnj
{
	meta:
		description = "Lockless Intro Pack"
	strings:
		$a = {B80030CD213C0373??0E1FBA????B409CD210633C050CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
