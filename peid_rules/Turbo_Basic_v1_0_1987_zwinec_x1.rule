rule _Turbo_Basic_v1_0_1987_zwinec
{
	meta:
		description = "Turbo Basic v1_0 1987"
	strings:
		$a = {2E8C??????2EC7}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
