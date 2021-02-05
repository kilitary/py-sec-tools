rule _PEnguinCrypt_v1_0_bpcnxe
{
	meta:
		description = "PEnguinCrypt v1_0"
	strings:
		$a = {B893????0055506764FF360000676489260000BD4B484342B804000000CC3C0475049090C39067648F060000585DBB0000400033C933C0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
