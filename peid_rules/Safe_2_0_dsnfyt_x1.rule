rule _Safe_2_0_dsnfyt
{
	meta:
		description = "Safe 2_0"
	strings:
		$a = {83EC10535657E8C40100}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
