rule _Hardlock_dongle_Alladin__bflplf
{
	meta:
		description = "Hardlock dongle _Alladin_"
	strings:
		$a = {5C5C2E5C484152444C4F434B2E565844000000005C5C2E5C46456E7465446576}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
