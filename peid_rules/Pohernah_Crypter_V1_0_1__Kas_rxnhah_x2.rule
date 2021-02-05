rule _Pohernah_Crypter_V1_0_1__Kas_rxnhah
{
	meta:
		description = "Pohernah Crypter V1_0_1 __ Kas"
	strings:
		$a = {60E8000000005D81ED2A27400031C04083F006403D401F00007507BE6A274000EB02EBEB8B859E28400083F801751731C001EE3D99000000740C8B8D86284000300E4046EBED}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
