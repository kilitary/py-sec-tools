rule _ACProtect_V1_4X__risco_kbxigp
{
	meta:
		description = "ACProtect V1_4X __ risco"
	strings:
		$a = {60E8010000007C83042406C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
