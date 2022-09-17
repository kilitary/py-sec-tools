rule _Armadillo_v1_72__v1_73_fsasxv
{
	meta:
		description = "Armadillo v1_72 _ v1_73"
	strings:
		$a = {558BEC6AFF68E8C1????68F486????64A1????????50648925????????83EC58}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
