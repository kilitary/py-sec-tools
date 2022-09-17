rule _StarForce_V1_X_V3_X__StarForce_Copy_Protection_System_vbdara
{
	meta:
		description = "StarForce V1_X_V3_X __ StarForce Copy Protection System"
	strings:
		$a = {68????????FF25????????0000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
