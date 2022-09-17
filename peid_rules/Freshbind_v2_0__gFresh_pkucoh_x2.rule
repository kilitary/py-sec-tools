rule _Freshbind_v2_0__gFresh_pkucoh
{
	meta:
		description = "Freshbind v2_0 __ gFresh"
	strings:
		$a = {64A1000000005589E56AFF6810304000689A1040}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
