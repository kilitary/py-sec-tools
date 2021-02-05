rule _JAM_v2_11_crbhjv
{
	meta:
		description = "JAM v2_11"
	strings:
		$a = {50061607BE????8BFEB9????FDFAF32EA5FB06BD????55CB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
