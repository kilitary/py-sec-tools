rule _VIRUS__I_Worm_KLEZ_thjgox
{
	meta:
		description = "VIRUS _ I_Worm_KLEZ"
	strings:
		$a = {558BEC6AFF6840D240??6804AC40??64A1????????50648925????????83EC585356578965E8FF15BCD0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
