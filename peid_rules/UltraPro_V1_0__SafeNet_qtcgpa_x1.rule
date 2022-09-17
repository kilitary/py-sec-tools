rule _UltraPro_V1_0__SafeNet_qtcgpa
{
	meta:
		description = "UltraPro V1_0 __ SafeNet"
	strings:
		$a = {A1????????85C00F853B0600005556C705????????01000000FF15}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
