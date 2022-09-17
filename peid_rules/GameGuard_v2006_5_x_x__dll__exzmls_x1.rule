rule _GameGuard_v2006_5_x_x__dll__exzmls
{
	meta:
		description = "GameGuard v2006_5_x_x ___dll_"
	strings:
		$a = {31FF740661E94A4D5030BA4C000000807C2408010F85??01000060BE00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
