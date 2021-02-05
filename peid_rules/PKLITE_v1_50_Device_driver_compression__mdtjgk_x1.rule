rule _PKLITE_v1_50_Device_driver_compression__mdtjgk
{
	meta:
		description = "PKLITE v1_50 _Device driver compression_"
	strings:
		$a = {B409BA1401CD21B8004CCD21F89C505351525657551E06BB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
