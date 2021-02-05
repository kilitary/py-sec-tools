rule _Freshbind_v2_0__gFresh_phzwwl
{
	meta:
		description = "Freshbind v2_0 __ gFresh"
	strings:
		$a = {64A1000000005589E56AFF681CA04100}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
