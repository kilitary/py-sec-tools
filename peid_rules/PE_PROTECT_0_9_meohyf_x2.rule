rule _PE_PROTECT_0_9_meohyf
{
	meta:
		description = "PE_PROTECT 0_9"
	strings:
		$a = {061E508CC88ED8BA7003B82425CD21??????????90B42FCD2153}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
