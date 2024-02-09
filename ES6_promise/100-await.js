import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const picRes = await uploadPhoto('profile-photo');
    const userRes = await createUser();
    return { photo: picRes, user: userRes };
  } catch (error) {
    console.error(error);
    return { photo: null, user: null };
  }
}
