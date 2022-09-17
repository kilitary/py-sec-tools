rule _PKLITE_v1_00_v1_03_lytbsu
{
	meta:
		description = "PKLITE v1_00_ v1_03"
	strings:
		$a = {B8????BA????8CDB03D83B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
