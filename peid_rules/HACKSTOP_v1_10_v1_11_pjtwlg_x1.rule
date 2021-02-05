rule _HACKSTOP_v1_10_v1_11_pjtwlg
{
	meta:
		description = "HACKSTOP v1_10_ v1_11"
	strings:
		$a = {B430CD2186E03D????73??B42FCD21B0??B44CCD2150B8????58EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
