rule _UPX_0_72_urqxfw
{
	meta:
		description = "UPX 0_72"
	strings:
		$a = {60E80000000083CDFF31DB5E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
