rule _SDProtector_1_1x__Randy_Li_mtkemp
{
	meta:
		description = "SDProtector 1_1x __ Randy Li"
	strings:
		$a = {558BEC6AFF681D321305688888880864A1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
